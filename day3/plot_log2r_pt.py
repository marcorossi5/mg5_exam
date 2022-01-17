import argparse
from pathlib import Path
import numpy as np
from time import time as tm
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from saft.saft import SAF_File
from saft.saf_histo import check_histograms


fit_fn_msg = "log((S + B) / B) = p0 exp(-p1 * pT)"

def print_scipy_stats(sci_ps, sci_errs):
    """Print minimizing paraters. """
    print("*" * 40)
    print("Scipy minimizing function parameters")
    print("Fitting function:", fit_fn_msg)
    for i, (p, err) in enumerate(zip(sci_ps, sci_errs)):
        print(f"p{i:<24} = {p:>13.8f}  +/-   {err:<10.8f}")
    print("*" * 40)


def fit_f(x, p0, p1):
    """
    The fitting function.
    Parameters
    ----------
        - x: np.array, independent data
        - p0: float, origin intercept
        - p1: float, angular coefficient
    Returns
    -------
        - np.array, evaluated function points of shape=(nb data,)
    """
    return p0 + p1 * x


def f(x, p0, p1):
    """
    The function to be plotted.
    Parameters
    ----------
        - x: np.array, independent points of shape=(nb data,)
        - p0: float, origin intercept
        - p1: float, angular coefficient
    Returns
    -------
        - np.array, evaluated function points of shape=(nb data,)
    """
    return p0 + p1 * x

def main(dirname):
    """
    Parameters
    ----------
        - dirname: str, directory name with .saf files
    """
    # importing histograms
    sm_hist = SAF_File(dirname / "histos_sm.saf").get("pt")
    dm_hist = SAF_File(dirname / "histos_dm.saf").get("pt")
    check_histograms(sm_hist, dm_hist)

    # compute transverse momentum bin values
    cut = 50 if "50" in dirname.name else 200
    ptmin = sm_hist.xmin
    ptmax = sm_hist.xmax
    pts = sm_hist.bins[:-1]

    # compute the bulk distribution
    bulk_min = 50 if cut == 50 else 200
    bulk_max = 250 if cut == 50 else 400
    mask = np.logical_and(pts>=bulk_min, pts<bulk_max)

    bkg = sm_hist.data # backgroud
    sig = dm_hist.data # signal

    # compute double log of signal to background ratio r
    r = np.divide(sig + bkg, bkg, out=np.ones_like(bkg), where=bkg!=0)
    logr = np.log(r)
    log2r = np.log(logr, out=np.zeros_like(logr), where=logr!=0)

    # fit with SciPy
    sci_ps, sci_cov = curve_fit(fit_f, pts[mask], log2r[mask])
    sci_errs = np.sqrt(np.diag(sci_cov))
    print_scipy_stats(sci_ps, sci_errs)

    x = np.linspace(ptmin, ptmax, 1000)

    # plot the error bands on the fitted function
    ps = np.linspace(-1, 1, 10)

    fig = plt.figure(figsize=[8, 6], dpi=100)
    ax = fig.add_subplot()
    mean_f = f(x, sci_ps[0], sci_ps[1])
    lower_f = f(x, sci_ps[0] - sci_errs[0], sci_ps[1] - sci_errs[1])
    upper_f = f(x, sci_ps[0] + sci_errs[0], sci_ps[1] + sci_errs[1])
    msg1 = r"$R = %.4f \pm %.4f$" % (sci_ps[0], sci_errs[0])
    msg2 = r"$(k_1-k_2) = %.4f \pm %.4f$ GeV$^{-1}$" % (sci_ps[1], sci_errs[1])
    ax.scatter(
        pts,
        log2r,
        s=5,
        marker=".",
        label="mg5",
        color="blue",
    )
    ax.fill_between(x, lower_f, upper_f, color="green", alpha=0.5, label=msg1)
    ax.fill_between([], [], color="white", label=msg2)
    ax.plot(x, mean_f, color="red", lw=0.5)
    ax.set_xlim(bulk_min, bulk_max)
    ax.legend()
    ax.tick_params(which="both", direction="in", top=True, right=True)
    ax.minorticks_on()
    fig.suptitle(r"$p + p \rightarrow j + X_{inv} $,     $p_T > %d$ GeV"%cut, y=0.96)
    ax.set_title(r"Linear interpolation: y = R + $(k_1-k_2) \,p_T$")
    ax.set_ylabel(r"$\log (\log (r))$")
    ax.set_xlabel(r"$p_{T,j}$ [GeV]")
    plt.savefig(dirname/"log2r(pT).png", dpi=300, bbox_inches="tight")
    plt.close()



if __name__ == "__main__":
    start = tm()
    parser = argparse.ArgumentParser()
    parser.add_argument("dirname", type=Path, help="directory name with .saf files")
    args = parser.parse_args()
    main(args.dirname)
    print(f"Program done in {tm()-start}s")
