from typing import DefaultDict


INPUT_FILE = "input"


def get_input():
    with open(INPUT_FILE) as f:
        return [int(x) for line in f.readlines() for x in line.split(",")]


def pt_one():
    f1 = get_input()

    for day in range(1, 81):
        for i in range(len(f1)):
            fish = f1[i]
            if fish == 0:
                f1.append(8)
                f1[i] = 6
            else:
                f1[i] = f1[i] - 1

    return len(f1)


def pt_two():
    f1 = get_input()

    counts = DefaultDict(int)
    for num in f1:
        counts[num] += 1

    print(counts)

    for day in range(1, 257):
        respawning = counts[0]
        for i in range(1, 9):
            counts[i - 1] = counts[i]

        counts[8] = respawning
        counts[6] += respawning

    return sum([counts[x] for x in counts])


print(pt_one())
print(pt_two())
