from typing import DefaultDict


INPUT_FILE = "input"


def get_input():
    with open(INPUT_FILE) as f:
        return [int(x) for line in f.readlines() for x in line.split(",")]


def get_counts(days):
    f1 = get_input()

    counts = DefaultDict(int)
    for num in f1:
        counts[num] += 1

    for day in range(1, days + 1):
        respawning = counts[0]
        for i in range(1, 9):
            counts[i - 1] = counts[i]

        counts[8] = respawning
        counts[6] += respawning

    return sum([counts[x] for x in counts])


print("Part #1: ", get_counts(80))
print("Part #2: ", get_counts(256))
