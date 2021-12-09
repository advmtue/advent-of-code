import heapq
from functools import reduce

INFILE = "input"


def get_input():
    with open(INFILE) as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


def pt_one():
    heights = get_input()

    risk_levels = []
    for yi, y in enumerate(heights):
        for xi, x in enumerate(heights[yi]):
            u = yi - 1
            d = yi + 1
            l = xi - 1
            r = xi + 1

            if u >= 0 and heights[u][xi] <= x:
                continue

            if d < len(heights) and heights[d][xi] <= x:
                continue

            if l >= 0 and heights[yi][l] <= x:
                continue

            if r < len(y) and heights[yi][r] <= x:
                continue

            risk_levels.append(x + 1)

    return sum(risk_levels)


def get_cluster_size_and_mark(heights, startx, starty):
    # Edge cases
    if starty < 0 or starty >= len(heights):
        return 0

    if startx < 0 or startx >= len(heights[starty]):
        return 0

    # Already in a cluster
    if heights[starty][startx][0]:
        return 0

    # Edge of a cluster
    if heights[starty][startx][1] == 9:
        return 0

    # Mark as in a cluster
    heights[starty][startx][0] = True

    # Combine with cluster size
    return (
        1
        + get_cluster_size_and_mark(heights, startx - 1, starty)
        + get_cluster_size_and_mark(heights, startx + 1, starty)
        + get_cluster_size_and_mark(heights, startx, starty - 1)
        + get_cluster_size_and_mark(heights, startx, starty + 1)
    )


def pt_two():
    heights = [
        [[False, height] for x, height in enumerate(yy)]
        for y, yy in enumerate(get_input())
    ]

    cluster_sizes = []

    for y, line in enumerate(heights):
        for x, height in enumerate(line):
            # Already marked as in cluster
            if height[0]:
                continue

            # 9 is never in cluster
            if height[1] == 9:
                continue

            cluster_sizes.append(get_cluster_size_and_mark(heights, x, y))

    return reduce(lambda a, c: a * c, heapq.nlargest(3, cluster_sizes), 1)


print(pt_one())
print(pt_two())
