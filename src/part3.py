from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
import numpy as np

from load_foil import load_foil
from part1 import create_cubic_interpolation_function
from part2 import integration_n_romberg


def get_length(fp, T):
    # Romberg's integration converges quite fast so N = 10 should be enough
    return integration_n_romberg(lambda x: np.sqrt(1 + fp(x) ** 2), 0, T, 10)


def plot_airflow(file):
    dim, ex, ey, ix, iy = load_foil(file)

    h_min = min(iy)
    h_max = max(ey)
    T = 1
    
	
    cs_i = create_cubic_interpolation_function(ix, iy)
    xs = np.linspace(0, 1, 100)
    _, ax = plt.subplots(figsize=(6.4, 4.8))
    ax.plot(ex, ey, c='r', marker='o', label='data_e')
    ax.plot(ix, iy, c='b', marker='o', label='data_i')
    Y_i = list(map(cs_i, xs))
    ax.plot(xs, Y_i, label="S_i")
    cs_e = create_cubic_interpolation_function(ex, ey)
    Y_e = list(map(cs_e, xs))
    ax.plot(xs, Y_e, label="S_e")
    plt.ylim(20 * h_min, 3 * h_max)
    plt.xlim(min(xs), max(xs))

    parameter_lambda = np.linspace(0, 1, 15)
    for option in parameter_lambda:
        airflow = (1 - option) * np.array(list(map(cs_e, xs))) + \
            option * 3 * h_max
        plt.plot(xs, airflow, 'grey')
    for option in parameter_lambda:
        airflow = -((option - 1) * np.array(list(map(cs_i, xs))) +
                    option * 3 * h_max)
        plt.plot(xs, airflow, 'grey')

    plt.tight_layout()
    plt.show()


def plot_pressure(file):
    dim, ex, ey, ix, iy = load_foil(file)
    h_min = min(iy)
    h_max = max(ey)
    T = 1
    cs_i = create_cubic_interpolation_function(ix, iy)
    cs_e = create_cubic_interpolation_function(ex, ey)
    xs = np.linspace(0, T, 100)
    static_pressure = 26436.27
    density = 0.4135

    def get_pressure_of_line(f):
        return static_pressure + 0.5 * density * get_length(f, T) ** 2

    parameter_lambda = np.linspace(0, 1, 500)
    pressures = []
    ys = []
    for option in parameter_lambda:
        airflow = (1 - option) * np.array(list(map(cs_e, xs))) + \
            option * 3 * h_max
        ys.append(airflow.tolist())
        pressures.append(get_pressure_of_line(
            lambda x: (1 - option) * cs_e(x, 1)))

    for option in parameter_lambda:
        airflow = -1 * ((option - 1) *
                        np.array(list(map(cs_i, xs))) + option * 3 * h_max)
        ys.append(airflow.tolist())
        pressures.append(get_pressure_of_line(
            lambda x: -((option - 1) * cs_i(x, 1))))
    segs = [np.column_stack([xs, y]) for y in ys]
    fig, ax = plt.subplots()
    ax.set_xlim(np.min(xs), np.max(xs))
    ax.set_ylim(np.min(ys), np.max(ys))
    line_segments = LineCollection(segs, array=pressures,
                                   linewidths=(0.5, 1, 1.5, 2),
                                   linestyles='solid')
    ax.add_collection(line_segments)
    axcb = fig.colorbar(line_segments)
    axcb.set_label('Pressure')
    ax.set_facecolor('gray')
    plt.sci(line_segments)
    plt.set_cmap('hot')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_airflow('datasets/goe05k.dat')
    plot_pressure('datasets/goe05k.dat')
