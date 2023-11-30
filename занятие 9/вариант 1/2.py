def I_maxx(a):
    maxx = max(a)
    i = a.index(maxx)
    return i

def I_minn(a):
    minn = min(a)
    j = a.index(minn)
    return j

def F(a, k1, k2):
    a[k1], a[k2] = a[k2], a[k1]

def R(MATRIX):
    for a in MATRIX:
        i = I_maxx(a)
        j = I_minn(a)
        F(a, 0, j)
        F(a, -1, i)
MATRIX = [
    [3, 7, 9, 2],
    [5, 1, 4, 6],
    [8, 2, 0, 3]
]
R(MATRIX)
for a in MATRIX:
    print(a)
