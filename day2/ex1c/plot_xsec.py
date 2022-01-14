from time import time as tm
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

fit_fn_msg = "y = p0 + p1 * log(x)"

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
    return p0 + p1 * np.log(x)

def main():
    mb = np.array([1.0, 1.7, 2.8, 4.6, 7.7, 12.9, 21.5, 35.9, 59.9, 100.0])
    xsec, unc = (
        np.loadtxt("cross_section_eex_bbxg_Egmin0.01.txt", dtype=str).T[2:4].astype(float)
    )

    # fit with SciPy
    p0 = (0.8, -0.3)
    bounds = ([0.0, -1.0], [1.0, 0.0])
    sci_ps, sci_cov = curve_fit(fit_f, np.log(mb), xsec, p0=p0, bounds=bounds)
    sci_errs = np.sqrt(np.diag(sci_cov))
    print_scipy_stats(sci_ps, sci_errs)

    x = np.linspace(1, 105, 1000)

    # plot the error bands on the fitted function
    ps = np.linspace(-1, 1, 10)

    fig = plt.figure(figsize=[8, 6], dpi=100)
    ax = fig.add_subplot()
    mean_f = f(x, sci_ps[0], sci_ps[1])
    lower_f = f(x, sci_ps[0] - sci_errs[0], sci_ps[1] - sci_errs[1])
    upper_f = f(x, sci_ps[0] + sci_errs[0], sci_ps[1] + sci_errs[1])
    msg1 = r"$m = %.3f \pm %.3f$" % (sci_ps[0], sci_errs[0])
    msg2 = r"$q = %.3f \pm %.3f$ [GeV]" % (sci_ps[1], sci_errs[1])
    ax.errorbar(
        mb,
        xsec,
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
    ax.set_xscale("log")
    ax.legend()
    ax.tick_params(which="both", direction="in", top=True, right=True)
    ax.minorticks_on()
    fig.suptitle(r"$e^+ e^- \rightarrow b \bar{b} g$", y=0.96)
    ax.set_title(r"Linear interpolation: y = $m \,\log(x)+q$")
    ax.set_ylabel(r"$\sigma$ [pb]")
    ax.set_xlabel(r"$m_b$ [GeV]")
    plt.savefig("xsec(mb).png", dpi=300, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    start = tm()
    main()
    print(f"Program done in {tm()-start}s")