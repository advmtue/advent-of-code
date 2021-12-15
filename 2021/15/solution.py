import math
from heapq import heappush, heappop
from typing import List, Tuple

M = []
with open("input") as f:
    for line in f:
        M.append([int(x) for x in line.strip()])


XM0 = len(M[0])
XMAX = 5 * len(M[0])
YM0 = len(M)
YMAX = 5 * len(M)


def get_dist(x, y):
    if not 0 <= x < XMAX:
        return None

    if not 0 <= y < YMAX:
        return None

    xadd = math.floor(x / XM0)
    yadd = math.floor(y / YM0)
    val = M[y % YM0][x % XM0] + xadd + yadd

    if val > 9:
        val -= 9

    return val


c = (0, 0)
D = {}
D[c] = (0, (-1, -1))
V = {}
h: List[Tuple[int, Tuple[int, int]]] = []

count = 0
while True:
    u = (c[0], c[1] - 1)
    d = (c[0], c[1] + 1)
    l = (c[0] - 1, c[1])
    r = (c[0] + 1, c[1])

    # Unvisited neighbors
    u_neigh = [
        x for x in [u, d, l, r] if 0 <= x[0] < XMAX and 0 <= x[1] < YMAX and x not in V
    ]

    for p in u_neigh:
        dist = D[c][0] + get_dist(*p)
        if p not in D or D[p][0] > dist:
            D[p] = (dist, c)
            heappush(h, (dist, p))

    V[c] = True

    m = heappop(h)[1]

    if m == (XMAX - 1, YMAX - 1):
        break

    c = m


print(D[(5 * len(M) - 1, 5 * len(M) - 1)][0])
