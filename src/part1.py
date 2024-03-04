import numpy as np


# ! Taken from chapter 3.3 of Numerical Recipes
def _compute_y2(X, Y, y0=None, yn=None):
    n = X.shape[0]
    y2 = np.zeros(n)
    u = np.zeros(n)
    if y0 is None:
        y2[0] = 0
        u[0] = 0
    else:
        y2[0] = -0.5
        u[0] = (3 / (X[1] - X[0])) * ((Y[1] - Y[0]) / (X[1] - X[0]) - y0)

    for i in range(1, n - 1):
        sig = (X[i] - X[i - 1]) / (X[i + 1] - X[i - 1])
        p = sig * y2[i - 1] + 2.0
        y2[i] = (sig - 1.0) / p
        u[i] = (Y[i + 1] - Y[i]) / (X[i + 1] - X[i]) - \
            (Y[i] - Y[i - 1]) / (X[i] - X[i - 1])
        u[i] = (6.0 * u[i] / (X[i + 1] - X[i - 1]) - sig * u[i - 1]) / p

    if yn is None:
        qn = 0
        un = 0
    else:
        qn = 0.5
        un = (3.0 / (X[n - 1] - X[n - 2])) * \
            (yn - (Y[n - 1] - Y[n - 2]) / (X[n - 1] - X[n - 2]))
    y2[n - 1] = (un - qn * u[n - 2]) / (qn * y2[n - 2] + 1.0)
    for k in reversed(range(n - 1)):
        y2[k] = y2[k] * y2[k + 1] + u[k]

    return y2


def _search_range(x, X):
    left = 0
    right = X.shape[0] - 1
    while left <= right:
        m = (left + right) // 2
        if X[m] == x:
            return m
        if x < X[m]:
            right = m - 1
        elif x > X[m]:
            left = m + 1
    return right


def create_cubic_interpolation_function(X, Y, y0=None, yn=None):
    assert (X.shape == Y.shape)
    y2 = _compute_y2(X, Y, y0, yn)
    cache = {}

    def actual_interp(x, derive=0):
        if x in cache:
            i = cache[x]
        else:
            i = _search_range(x, X)
            cache[x] = i
        if x == X[i]:
            return Y[i]
        if (i < 0) or (i + 1 >= X.shape[0]):
            raise Exception("x out of bounds")
        h = X[i + 1] - X[i]
        if h == 0:
            raise Exception("Bad input")
        a = (X[i + 1] - x) / h
        b = (x - X[i]) / h
        if derive <= 0:
            y = a * Y[i] + b * Y[i + 1] + \
                ((a ** 3 - a) * y2[i] + (b ** 3 - b) * y2[i + 1]) * (h * h) / 6
        elif derive == 1:
            y = ((Y[i + 1] - Y[i]) / h) + (h / 6) * \
                (y2[i] * (1 - 3 * a * a) + y2[i + 1] * (3 * b * b - 1))
        elif derive == 2:
            y = a * y2[i] + b * y2[i + 1]
        else:
            raise Exception("Cannot derive after second order")
        return y

    return actual_interp
