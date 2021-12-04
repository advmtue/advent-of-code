import numpy as np
from scipy.stats import mode

INPUT_FILE = "input"


def get_input():
    with open(INPUT_FILE) as f:
        return [list(x.strip()) for x in f.readlines()]


def pt_one(numbers):
    g = "".join(mode(f)[0][0] for f in np.transpose(numbers))
    e = "".join("1" if f == "0" else "0" for f in g)

    return int(g, 2) * int(e, 2)


def get_filtered_recursive(numbers, is_highest, bitpos) -> int:
    # Base case
    if len(numbers) == 1:
        return int("".join(numbers[0]), 2)

    # Extract mode and it's count
    vals, counts = mode(np.transpose(numbers)[bitpos])
    m = vals[0]
    count = counts[0]

    # Invert if searching for least common
    if not is_highest:
        m = "1" if m == "0" else "0"

    # Tiebreaker: common item is 50% of the array
    if count == len(numbers) / 2:
        m = "1" if is_highest else "0"

    # Recursive step: Filter
    return get_filtered_recursive(
        [l for l in numbers if l[bitpos] == m], is_highest, bitpos + 1
    )


def pt_two(numbers):
    co2 = get_filtered_recursive(numbers, is_highest=True, bitpos=0)
    o2 = get_filtered_recursive(numbers, is_highest=False, bitpos=0)

    return co2 * o2


if __name__ == "__main__":
    print("Part one: ", pt_one(get_input()))
    print("Part two: ", pt_two(get_input()))
