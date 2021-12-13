INFILE = "input"

I = []
C = []
with open(INFILE) as f:
    for line in f:
        if line == "\n":
            break

        s = line.strip().split(",")
        I.append((int(s[0]), int(s[1])))

    for command in f:
        cmd = command.strip().split(" ")[2].split("=")
        C.append((cmd[0], int(cmd[1])))


count = None
for axis, num in C:
    idx = 0 if axis == "x" else 1

    for i, pos in enumerate(I):
        if pos[idx] > num:
            # Fold candidate
            coords = list(pos)
            coords[idx] = num - abs(num - coords[idx])
            I[i] = (coords[0], coords[1])

    if count is None:
        count = len(set(I))

print(count)

# Part 2
maxy = max(x[1] for x in I)
maxx = max(x[0] for x in I)

for y in range(maxy + 1):
    for x in range(maxx + 1):
        if (x, y) in I:
            print("#", end="")
        else:
            print(" ", end="")

    print()
