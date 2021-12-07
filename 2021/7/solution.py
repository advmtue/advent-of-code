from typing import DefaultDict


INPUT_FILE = "input"


def get_input():
    with open(INPUT_FILE) as f:
        return [int(x) for line in f.readlines() for x in line.split(",")]


f1 = get_input()


def fuel_cost(start, stop):
    difference = abs(start - stop)
    return int(difference * ((difference + 1) / 2))


totals = DefaultDict(int)
for i in range(max(f1)):
    for num in f1:
        totals[i] += fuel_cost(num, i)


tmin = None
imin = -1
for i in totals:
    if tmin == None or totals[i] <= tmin:
        tmin = totals[i]
        imin = i

print(imin, totals[imin])
