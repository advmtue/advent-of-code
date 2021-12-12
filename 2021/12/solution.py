import collections
from typing import DefaultDict


INFILE = "input"

I = []
with open(INFILE) as f:
    I = [line.strip().split("-") for line in f.readlines()]

C = DefaultDict(list)
for pair in I:
    C[pair[0]].append(pair[1])
    C[pair[1]].append(pair[0])


def count_traversals(current, been_to=[]):
    if current == "end":
        return 1

    if current == "start":
        return 0

    nbt = been_to
    if current.islower():
        nbt = nbt + [current]

    counts = collections.Counter(nbt)
    no_revisit = 2 in counts.values()

    options = 0
    for path in C[current]:
        if no_revisit and path in nbt:
            continue

        options += count_traversals(path, nbt)

    return options


paths = 0
for path in C["start"]:
    paths += count_traversals(path)

print(paths)
