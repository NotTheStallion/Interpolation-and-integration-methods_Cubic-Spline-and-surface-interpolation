import sys
import numpy as np
import re  # regexp


################################################################
# Airfoil : load profile of a wing
#
# Reads a file whose lines contain coordinates of points,
# separated by an empty line.
# Every line not containing a couple of floats is discarded.
# Returns a couple constitued of the list of points of the
# extrados and the intrados.
def load_foil(file):
    f = open(file, 'r')
    def matchline(line): return re.match(r"\s*([\d\.-]+)\s*([\d\.-]+)", line)
    extra = []
    intra = []
    rextra = False
    rintra = False
    rheader = False
    for line in f:
        m = matchline(line)
        if m is None:
            if not rheader:
                rheader = True
            elif not rextra:
                rextra = True
            elif not rintra:
                rintra = True
            continue
        if (m is not None) and rheader and not rextra and not rintra:
            dim = np.array(list(map(lambda t: float(t), m.groups())))
            continue
        if (m is not None) and rheader and rextra and not rintra:
            extra.append(m.groups())
            continue
        if (m is not None) and rheader and rextra and rintra:
            intra.append(m.groups())
            continue
    ex = np.array(list(map(lambda t: float(t[0]), extra)))
    ey = np.array(list(map(lambda t: float(t[1]), extra)))
    ix = np.array(list(map(lambda t: float(t[0]), intra)))
    iy = np.array(list(map(lambda t: float(t[1]), intra)))
    return dim, ex, ey, ix, iy


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please provide a input file")
        exit(1)

    (dim, ex, ey, ix, iy) = load_foil(sys.argv[1])
    print(dim)
    print(ex)
    print(ey)
    print(ix)
    print(iy)
