INFILE = "input"


def get_input():
    with open(INFILE) as f:
        return [x.strip() for x in f.readlines()]


def in_graph(I, x, y):
    if x < 0 or y < 0:
        return False

    if x >= len(I) or y >= len(I):
        return False

    return True


I = [[[int(x), False] for x in l] for l in get_input()]

flash_count = 0
first_all_flash = None
i = 0
while i < 100 or not first_all_flash:
    # Increase energy levels
    for yi, y in enumerate(I):
        for xi, x in enumerate(y):
            I[yi][xi][0] += 1

    # Look for flashes
    flash_occurred = True
    while flash_occurred:
        flash_occurred = False
        for yi, y in enumerate(I):
            for xi, x in enumerate(y):
                if x[0] > 9 and not x[1]:
                    # Flash!
                    flash_occurred = True
                    if i < 100:
                        flash_count += 1

                    I[yi][xi][1] = True

                    if in_graph(I, xi - 1, yi - 1):
                        I[yi - 1][xi - 1][0] += 1
                    if in_graph(I, xi, yi - 1):
                        I[yi - 1][xi][0] += 1
                    if in_graph(I, xi + 1, yi - 1):
                        I[yi - 1][xi + 1][0] += 1

                    if in_graph(I, xi - 1, yi):
                        I[yi][xi - 1][0] += 1
                    if in_graph(I, xi + 1, yi):
                        I[yi][xi + 1][0] += 1

                    if in_graph(I, xi - 1, yi + 1):
                        I[yi + 1][xi - 1][0] += 1
                    if in_graph(I, xi, yi + 1):
                        I[yi + 1][xi][0] += 1
                    if in_graph(I, xi + 1, yi + 1):
                        I[yi + 1][xi + 1][0] += 1

    # If we haven't encountered the all-flash moment, calculate if it is now
    if not first_all_flash:
        tfc = len([x for y in I for x in y if x[1]])
        if tfc == 100:
            first_all_flash = i + 1

    # Reset flashed fish to 0
    for yi, y in enumerate(I):
        for xi, x in enumerate(y):
            if x[1]:
                I[yi][xi] = [0, False]

    i += 1


print("Part #1:", flash_count)
print("Part #2:", first_all_flash)
