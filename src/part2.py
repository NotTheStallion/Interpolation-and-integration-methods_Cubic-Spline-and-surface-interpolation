import matplotlib.pyplot as plt
import numpy as np


def integration_n_trapezoidal(f, a, b, N):
    h = (b - a) / N  # width of each trapezoid
    res = 0.

    for i in range(N):
        xi = a + i * h
        res += h * (f(xi) + f(xi + h)) / 2.
    return res


def integration_n_simpson(f, a, b, N):
    h = (b - a) / N
    res = 0.

    for i in range(N):
        xi = a + i * h
        res += h * (f(xi) + 4 * f(xi + h / 2.) + f(xi + h)) / 6.
    return res


def integration_n_romberg(f, a, b, N):
    R = np.zeros((N, N))
    R[0, 0] = (b - a) * (f(a) + f(b)) / 2.

    pow2 = 2
    for n in range(1, N):
        R[n, 0] = integration_n_trapezoidal(f, a, b, pow2)
        pow2 *= 2
        pow4 = 4
        for m in range(1, n + 1):
            R[n, m] = (pow4 * R[n, m - 1] - R[n - 1, m - 1]) / (pow4 - 1)
            pow4 *= 4
    return R[N - 1, N - 1]


def integration_epsilon(f, a, b, eps, meth):
    N = 10
    R = np.zeros((N, N))
    R[0, 0] = meth(f, a, b, N)

    pow2 = 2
    for n in range(1, N):
        R[n, 0] = meth(f, a, b, pow2)
        pow2 *= 2
        pow4 = 4
        for m in range(1, n + 1):
            R[n, m] = (pow4 * R[n, m - 1] - R[n - 1, m - 1]) / (pow4 - 1)
            pow4 *= 4
        if abs(R[n, n] - R[n - 1, n - 1]) < eps:
            return R[n, n]
    return R[N - 1, N - 1]


if __name__ == '__main__':
    def g(x): return 1. / (1. + x ** 2)
    expected = 1.89254688
    a, b = -1., 2.

    errors = []
    for n in range(1, 21):
        errors.append(abs(expected - integration_n_trapezoidal(g, a, b, n)))
    plt.plot(errors, marker='x', label='Trapezoidal')
    errors = []
    for n in range(1, 21):
        errors.append(abs(expected - integration_n_simpson(g, a, b, n)))
    plt.plot(errors, marker='x', label='Simpson')
    errors = []
    for n in range(1, 21):
        errors.append(abs(expected - integration_n_romberg(g, a, b, n)))
    plt.plot(errors, marker='x', label='Romberg')

    plt.xlabel("Number of iterations")

    plt.yscale('log')
    plt.ylabel('Error')

    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
