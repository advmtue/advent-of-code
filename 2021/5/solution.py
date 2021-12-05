INPUT_FILE = "input"


def read_points_from_line(line: str):
    l1, l2 = line.strip().split("->")

    l1 = l1.strip()
    l2 = l2.strip()

    l1_points = tuple([int(x) for x in l1.split(",")])
    l2_points = tuple([int(x) for x in l2.split(",")])

    return tuple([l1_points, l2_points])


def get_input():
    with open(INPUT_FILE) as f:
        return [read_points_from_line(l) for l in f.readlines()]


# Return a list of points between two given points (p1 and p1)
def get_pts_between(p1, p2):
    pts = set()
    startx, starty = p1
    stopx, stopy = p2

    stepx = 1
    stepy = 1

    # Horizontal direction
    if startx > stopx:
        stepx = -1
    elif startx == stopx:
        stepx = 0

    # Vertical direction
    if starty > stopy:
        stepy = -1
    elif starty == stopy:
        stepy = 0

    # Skip horizontal movements if there is none
    if stepx != 0:
        for i, x in enumerate(range(startx, stopx, stepx)):
            newpt = [x, starty + (stepy * i)]
            pts.add(tuple(newpt))

    # Skip vertical movements if there is none
    if stepy != 0:
        for i, y in enumerate(range(starty, stopy, stepy)):
            newpt = [startx + (stepx * i), y]
            pts.add(tuple(newpt))

    # Add the final point
    pts.add(tuple([stopx, stopy]))

    return list(pts)


def count_line_intersects(pairs):
    field = {}

    for pair in pairs:
        pts = get_pts_between(pair[0], pair[1])

        for pt in pts:
            if pt not in field:
                field[pt] = 1
            else:
                field[pt] += 1

    return sum([1 for pt in field if field[pt] > 1])


def pt_one():
    # Filter: keep horizontal/vertical lines only
    h_or_v_points = [
        pts for pts in get_input() if pts[0][0] == pts[1][0] or pts[0][1] == pts[1][1]
    ]

    return count_line_intersects(h_or_v_points)


def pt_two():
    return count_line_intersects(get_input())


if __name__ == "__main__":
    print(pt_one())
    print(pt_two())
