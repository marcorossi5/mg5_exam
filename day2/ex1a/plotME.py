from time import time as tm
import numpy as np
import matplotlib.pyplot as plt

CF = 4 / 3
alphas = 0.118  # alpha(MZ)
PI = np.pi


def ddx_full_massive(x1, x2, rho):
    """
    The `e+ e- > q qbar g` differential cross section for fully massive final
    state.

    Parameters
    ----------
        - x1: np.array, quark energy fraction
        - x2: np.array, anti-quark energy fraction
        - rho: np.array, squared inverse gamma factor
    """
    beta = np.sqrt(1 - rho)
    return (
        CF / beta * alphas / (2 * PI) * (
            2 * (x1 + x2 - 1 - rho / 2) / ((1 - x1) * (1 - x2)) -
            rho / 2 * (1 / (1 - x1)** 2 + 1 / (1 - x2)** 2) +
            1 / (1 + rho / 2) * ((1 - x1)** 2 + (1 - x2)** 2) / ((1 - x1) * (1 - x2))
        )
    )


def ddx_soft_collinear(z, theta, rho):
    """
    The `e+ e- > q qbar g` differential cross section for soft and collinear
    approximation (gluon close to quark).

    Note: this function has a maximum for theta^2 = rho. This means that the
    maximum is reached for k_T = sqrt(rho * s) = 2*m.

    Parameters
    ----------
        - z: np.array, gluon energy fraction
        - theta: np.array, gluon-quark angle
        - rho: np.array, squared inverse gamma factor
    """
    
    return CF * alphas / PI * 1 / z * theta**2/(theta**2 + rho)**2


def main():
    """
    Plots differential distribution in the soft and collinear approximation as a
    function of the gluon transverse momentum, for different values of the quark
    mass in the final state.
    """
    s = 1
    Eg = 3e-3

    # rho = 4*(m**2) / s
    r_m0 = 0 # massless
    r_m1 = 4e-2 # massive, m = 0.1

    sqrts = np.sqrt(s)

    # kt = p * sin(theta) ~ p * theta
    # p is the modulus of the quark momentum. In the soft limit, it is equal to
    # the center of mass energy sqrts
    kt = np.linspace(1e-2, 1.5, 1000)
    z = 2 * Eg / sqrts
    # theta = kt / p
    theta = kt / sqrts

    x_m0 = ddx_soft_collinear(z, theta, r_m0) # massless
    x_m1 = ddx_soft_collinear(z, theta, r_m1) # massive

    # plt.rcParams.update({'text.usetex': True})

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(kt, x_m0, linestyle='dashed', alpha=0.8, color='blue', lw=1)
    ax.plot(kt, x_m1, color='lawngreen', lw=1)

    peak = np.sqrt(r_m1*s)
    ax.vlines(
        peak, 0, 80, ls=(0, (3, 7)), color='red', alpha=0.6,
        lw=0.5, linestyle='dotted'
    )

    ax.text(0.07, 30, 'dead cone', rotation='vertical', color='red', alpha=0.6, fontsize='xx-large')
    ax.text(0.47, 47, 'm = 0', color='blue', alpha=0.8, fontsize='x-large')
    ax.text(0.27, 15, 'm = 0.01', color='lawngreen', fontsize='x-large')

    fig.suptitle(r'$e^+ e^- \rightarrow Q \bar{Q} g$')
    ax.set_title(r'$\sqrt{s}=1 \quad E_g = 3 \cdot 10^{-3}$')
    ax.set_xlabel(r'$k_T$ [GeV]')
    ax.set_ylabel(r'$\frac{1}{\sigma^{LO}} \frac{d^2 \sigma}{dz \,d\theta^2}$')

    ax.tick_params(which="both", direction="in", top=True, right=True)
    ax.minorticks_on()

    ax.set_xlim(0, 1.5)
    ax.set_xticks(np.linspace(0, 1.5, 7))

    ax.set_ylim(0, 80)
    ax.set_yticks(np.linspace(0, 80, 5))

    plt.savefig("me(kt).png", dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    start = tm()
    main()
    print(f"Program done in {tm()-start}s")
