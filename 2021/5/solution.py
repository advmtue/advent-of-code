INPUT_FILE = "input"


def read_points_from_line(line: str):
    l1, l2 = line.strip().split("->")

    l1 = l1.strip()
    l2 = l2.strip()

    l1_points = tuple([int(x) for x in l1.split(",")])
    l2_points = tuple([int(x) for x in l2.split(",")])

    return [l1_points, l2_points]


def get_input():
    with open(INPUT_FILE) as f:
        return [read_points_from_line(l) for l in f.readlines()]


def get_pts_between(p1, p2):
    pts = []

    if p1[0] != p2[0]:
        start = p1[0]
        stop = p2[0]

        if stop < start:
            tmp = start
            start = stop
            stop = tmp

        stop += 1

        for x in range(start, stop):
            pts.append(tuple([x, p1[1]]))

        return pts

    if p1[1] != p2[1]:
        start = p1[1]
        stop = p2[1]

        if stop < start:
            tmp = start
            start = stop
            stop = tmp

        stop += 1

        for y in range(start, stop):
            pts.append(tuple([p1[0], y]))

        return pts

    return pts


def pt_one():
    h_or_v_points = [
        pts for pts in get_input() if pts[0][0] == pts[1][0] or pts[0][1] == pts[1][1]
    ]

    field = {}

    for pairs in h_or_v_points:
        pts = get_pts_between(pairs[0], pairs[1])

        for pt in pts:
            if pt not in field:
                field[pt] = 1
            else:
                field[pt] += 1

    count = 0
    for pt in field:
        if field[pt] > 1:
            count += 1

    return count


def get_pts_between_diag(p1, p2):
    pts = set()
    # Left to right
    startx, starty = p1
    stopx, stopy = p2

    stepx = 1
    stepy = 1

    if startx > stopx:
        stepx = -1
    elif startx == stopx:
        stepx = 0

    if starty > stopy:
        stepy = -1
    elif starty == stopy:
        stepy = 0

    if stepx != 0:
        for i, x in enumerate(range(startx, stopx, stepx)):
            newpt = [x, starty + (stepy * i)]
            pts.add(tuple(newpt))

    if stepy != 0:
        for i, y in enumerate(range(starty, stopy, stepy)):
            newpt = [startx + (stepx * i), y]
            pts.add(tuple(newpt))

    pts.add(tuple([stopx, stopy]))

    return list(pts)


def pt_two():
    pairs = get_input()
    field = {}

    for pair in pairs:
        pts = get_pts_between_diag(pair[0], pair[1])

        for pt in pts:
            if pt not in field:
                field[pt] = 1
            else:
                field[pt] += 1

    count = 0
    for pt in field:
        if field[pt] > 1:
            count += 1

    return count


if __name__ == "__main__":
    print(pt_one())
    print(pt_two())
