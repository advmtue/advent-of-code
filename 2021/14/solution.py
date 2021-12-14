from itertools import pairwise
import collections
from collections import defaultdict
from typing import DefaultDict

INFILE = "input"

START = ""
R = {}
with open(INFILE) as f:
    START = f.readline().strip()

    # ignore whitespace line
    f.readline()

    for line in f:
        line = line.strip().split(" -> ")
        pair = (line[0][0], line[0][1])
        r = line[1]
        R[pair] = r

# pt 2
S: DefaultDict = defaultdict(int)
C: DefaultDict = defaultdict(int)
for p in pairwise(START):
    S[p] += 1

for l in START:
    C[l] += 1

for i in range(40):
    n: DefaultDict = defaultdict(int)
    for k in S:
        c = R[k]
        C[c] += S[k]

        n[k] -= S[k]
        n[(k[0], c)] += S[k]
        n[(c, k[1])] += S[k]

    for k in n:
        S[k] += n[k]

        if S[k] <= 0:
            del S[k]

    if i == 9:
        most = max(C.values())
        least = min(C.values())
        print("Part #1:", most - least)


most = max(C.values())
least = min(C.values())
print("Part #2:", most - least)
