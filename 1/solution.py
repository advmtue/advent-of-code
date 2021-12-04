from functools import reduce
from itertools import pairwise
from typing import Tuple
from more_itertools.recipes import sliding_window


INPUT_FILE = "input"


def get_input():
    with open(INPUT_FILE) as f:
        return [int(line.strip()) for line in f.readlines()]


def accumulate(accumulator: int, current: Tuple[int, int]) -> int:
    return accumulator + 1 if current[0] < current[1] else accumulator


def count_sliding_window_increases(numbers, size=1):
    paired_sums = pairwise(
        (sum(x) for x in sliding_window(numbers, size))  # type:ignore
    )

    return reduce(accumulate, paired_sums, 0)


if __name__ == "__main__":
    print("part 1: ", count_sliding_window_increases(get_input(), 1))
    print("part 2: ", count_sliding_window_increases(get_input(), 3))
