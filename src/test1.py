import numpy as np
import scipy.interpolate as i

from load_foil import load_foil
from part1 import create_cubic_interpolation_function


def test_cubic_spline(path):
    print("test of cubic spline functions ...", end="")

    dim, ex, ey, ix, iy = load_foil(path)
    cs_i = i.CubicSpline(ix, iy, axis=0, bc_type='natural')
    cs_e = i.CubicSpline(ex, ey, axis=0, bc_type='natural')
    xs = np.linspace(0, 1, 100)
    scipy_cs_i = cs_i(xs)
    scipy_cs_e = cs_e(xs)

    cs_i = list(map(create_cubic_interpolation_function(ix, iy), xs))
    cs_e = list(map(create_cubic_interpolation_function(ex, ey), xs))

    list_e = np.isclose(cs_e, scipy_cs_e, rtol=1e-17, atol=1e-05)
    list_i = np.isclose(cs_i, scipy_cs_i, rtol=1e-17, atol=1e-06)

    list_e = np.all(list_e)
    list_i = np.all(list_i)

    if not list_i or not list_e:
        raise ValueError(f"Expected: {scipy_cs_i}, got: {cs_i}")
    print("\tOK")


def test_cubic_spline_derivative(path, eps=1e-2):
    print("test of cubic spline function with derivatives ...", end="")
    dim, ex, ey, ix, iy = load_foil(path)
    scipy_dcs = i.CubicSpline(ix, iy, axis=0, bc_type='natural').derivative(1)
    xs = np.linspace(0, 1, 100)
    my_dcs = create_cubic_interpolation_function(ix, iy)

    result = np.array(list(map(lambda x: my_dcs(x, 1), xs)))
    expected = scipy_dcs(xs)
    if np.sum(np.abs(expected - result)) > eps:
        raise ValueError(f"Expected: {expected}, got: {result}")
    print("\tOK")


if __name__ == '__main__':
    eps = 1

    # This function tests how good the CS is.
    # turn graph to True to plot the difference curve.
    test_cubic_spline('datasets/goe05k.dat')

    test_cubic_spline_derivative('datasets/goe05k.dat', eps)
