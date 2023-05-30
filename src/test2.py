import numpy as np

from part2 import integration_n_simpson, integration_n_trapezoidal, integration_n_romberg, integration_epsilon


def test_integration_simpson_result(f, a, b, N, expected, eps):
    print("Testing Simpson integration...", end="")

    res = integration_n_simpson(f, a, b, N)

    if abs(res - expected) > eps:
        raise ValueError(f"Expected: {expected}, got: {res}")

    print("\tOK")


def test_integration_trapezoidal_result(f, a, b, N, expected, eps):
    print("Testing Trapezoidal integration...", end="")

    res = integration_n_trapezoidal(f, a, b, N)

    if abs(res - expected) > eps:
        raise ValueError(f"Expected: {expected}, got: {res}")

    print("\tOK")


def test_integration_romberg_result(f, a, b, N, expected, eps):
    print("Testing Romberg integration...", end="")

    res = integration_n_romberg(f, a, b, N)

    if abs(res - expected) > eps:
        raise ValueError(f"Expected: {expected}, got: {res}")

    print("\tOK")


def test_integration_epsilon(f, a, b, eps, meth, expected):
    print("Testing Epsilon integration...", end="")

    res = integration_epsilon(f, a, b, eps, meth)

    if abs(res - expected) > eps:
        raise ValueError(f"Expected: {expected}, got: {res}")

    print("\tOK")


def test_methods(f, a, b, meth, N, expected, eps):
    print("Testing integration methods...", end="")

    res = meth(f, a, b, N)

    if abs(res - expected) > eps:
        raise ValueError(f"Expected: {expected}, got: {res}")

    print("\tOK")


if __name__ == '__main__':
    eps = 1e-6

    print("> Testing integration methods on f(x) = x^2 on [0, 1]\n")
    def f(x): return x ** 2
    expected = 1. / 3.
    a, b = 0, 1
    test_integration_trapezoidal_result(f, a, b, 1000, expected, eps)
    test_integration_simpson_result(f, a, b, 100, expected, eps)
    test_integration_romberg_result(f, a, b, 10, expected, eps)
    test_integration_epsilon(f, a, b, eps, integration_n_trapezoidal, expected)

    print("\n> Testing integration methods on f(x) = exp(-x^2) on [-10, 10]\n")
    def f(x): return np.exp(-x * x)
    expected = np.sqrt(np.pi)
    a, b = -10, 10
    test_integration_trapezoidal_result(f, a, b, 1000, expected, eps)
    test_integration_simpson_result(f, a, b, 100, expected, eps)
    test_integration_romberg_result(f, a, b, 10, expected, eps)
    test_integration_epsilon(f, a, b, eps, integration_n_trapezoidal, expected)

    print(
        "\n> Testing integration methods on f(x) = 1 / (1 + x^2) on [-1, 2]\n")

    def f(x): return 1. / (1. + x * x)
    expected = 1.89254688
    a, b = -1, 2
    test_integration_trapezoidal_result(f, a, b, 1000, expected, eps)
    test_integration_simpson_result(f, a, b, 100, expected, eps)
    test_integration_romberg_result(f, a, b, 10, expected, eps)
    test_integration_epsilon(f, a, b, eps, integration_n_trapezoidal, expected)

    print("\n> Testing integration methods on f(x) = cos(x) on [0, 2 * pi]\n")
    f = np.cos
    expected = 0.
    a, b = 0, 2 * np.pi
    test_integration_trapezoidal_result(f, a, b, 1000, expected, eps)
    test_integration_simpson_result(f, a, b, 100, expected, eps)
    test_integration_romberg_result(f, a, b, 10, expected, eps)
    test_integration_epsilon(f, a, b, eps, integration_n_trapezoidal, expected)

    print("\n> Testing integration methods on f(x) = sin(x) on [0, 2 * pi]\n")
    f = np.sin
    expected = 0.
    a, b = 0, 2 * np.pi
    test_integration_trapezoidal_result(f, a, b, 1000, expected, eps)
    test_integration_simpson_result(f, a, b, 100, expected, eps)
    test_integration_romberg_result(f, a, b, 10, expected, eps)
    test_integration_epsilon(f, a, b, eps, integration_n_trapezoidal, expected)
