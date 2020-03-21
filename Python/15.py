from math import factorial as F

def C(n, r):
    return F(n) // (F(n - r) * F(r))

def lattice_path(x, y):
    return C(x + y, x)

print(lattice_path(20, 20))
