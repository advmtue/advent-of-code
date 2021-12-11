INFILE = "input"

I = [[int(x) for x in l.strip()] for l in open(INFILE).readlines()]

flash_count = 0
first_all_flash = None
i = 0
while i < 100 or not first_all_flash:
    # Increase energy levels
    for yi, y in enumerate(I):
        for xi, x in enumerate(y):
            I[yi][xi] += 1

    # Look for flashes
    flash_occurred = True
    while flash_occurred:
        flash_occurred = False
        for yi, y in enumerate(I):
            for xi, x in enumerate(y):
                if x == 10:
                    I[yi][xi] += 1
                    flash_occurred = True

                    if i < 100:
                        flash_count += 1

                    # Neighbors
                    for dy in range(yi - 1, yi + 2):
                        for dx in range(xi - 1, xi + 2):
                            if 0 <= dy < len(I) and 0 <= dx < len(y) and I[dy][dx] < 10:
                                I[dy][dx] += 1

    if not first_all_flash:
        tfc = len([x for y in I for x in y if x > 9])
        if tfc == 100:
            first_all_flash = i + 1

    for yi, y in enumerate(I):
        for xi, x in enumerate(y):
            if x > 9:
                I[yi][xi] = 0

    i += 1


print("Part #1:", flash_count)
print("Part #2:", first_all_flash)
