import argparse
import numpy as np
from time import time as tm
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


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

def main(fname):
    """
    Parameters
    ----------
        - fname: str, input .saf filename
    """
    # compute transverse momentum bin values
    ptmin = 0
    ptmax = 500
    nbins = 252
    pts = np.linspace(ptmin, ptmax, nbins)
    bulk_min = 50
    bulk_max = 250
    mask = np.logical_and(pts>=bulk_min, pts<bulk_max)

    sigma_b = 6.486740e+02
    sigma_s = 3.203171e+00

    a = np.loadtxt(fname)
    underflow = a[0]
    overflow = a[-1]
    bkg = a[1:-1,0].astype(float) # backgroud
    sig = a[1:-1,1].astype(float) # signal

    # compute double log of signal to background ratio r
    r = np.divide(sig + bkg, bkg, out=np.ones_like(bkg), where=bkg!=0)
    logr = np.log(r)
    log2r = np.log(logr, out=np.zeros_like(logr), where=logr!=0)

    # fit with SciPy
    sci_ps, sci_cov = curve_fit(fit_f, pts[mask], log2r[mask[:-1]])
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
    msg1 = r"$R = %.3f \pm %.3f$ [GeV]" % (sci_ps[0], sci_errs[0])
    msg2 = r"$(k_1-k_2) = %.3f \pm %.3f$" % (sci_ps[1], sci_errs[1])
    ax.errorbar(
        pts[:-1],
        log2r,
        yerr=1e-2,
        linestyle="",
        marker=".",
        markersize=5,
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
    fig.suptitle(r"$p + p \rightarrow j + $ inv", y=0.96)
    ax.set_title(r"Linear interpolation: y = R + $(k_1-k_2) \,p_T$")
    ax.set_ylabel(r"$\log (\log (r))$ [pb]")
    ax.set_xlabel(r"$p_{T,j}$ [GeV]")
    plt.savefig("log2r(pT).png", dpi=300, bbox_inches="tight")
    plt.close()



if __name__ == "__main__":
    start = tm()
    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="input .saf filename")
    args = parser.parse_args()
    main(args.fname)
    print(f"Program done in {tm()-start}s")