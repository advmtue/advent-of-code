INFILE = "input"


def get_input():
    with open(INFILE) as f:
        return [[half.strip() for half in line.split("|")] for line in f.readlines()]


def pt_one():
    inputs = [x for h in get_input() for x in h[1].split(" ")]
    match = [2, 3, 4, 7]

    count = 0
    for word in inputs:
        if len(word) in match:
            count += 1

    return count


print(pt_one())
