from typing import Tuple


INPUT_FILE = "input"


def get_input():
    with open(INPUT_FILE) as f:
        return [line.strip() for line in f.readlines()]


def get_offset_for_direction(direction: str) -> Tuple[int, int]:
    command = direction.split(" ")[0]
    amount = direction.split(" ")[1]

    if command == "forward":
        return (int(amount), 0)
    elif command == "down":
        return (0, int(amount))
    elif command == "up":
        return (0, -int(amount))
    else:
        print("Unhandled command =", direction)
        return (0, 0)


def add_delta_to_position(
    pos: Tuple[int, int], delta: Tuple[int, int]
) -> Tuple[int, int]:
    return (pos[0] + delta[0], pos[1] + delta[1])


def handle_commands_pt1(directions: list[str]) -> int:
    start = (0, 0)

    for direction in directions:
        delta = get_offset_for_direction(direction)
        start = add_delta_to_position(start, delta)

    return start[0] * start[1]


def handle_commands_pt2(directions: list[str]) -> int:
    # horizontal, depth, aim
    current = (0, 0, 0)

    for direction in directions:
        command = direction.split(" ")[0]
        amount = int(direction.split(" ")[1])

        if command == "down":
            current = (current[0], current[1], current[2] + amount)
        elif command == "up":
            current = (current[0], current[1], current[2] - amount)
        elif command == "forward":
            current = (
                current[0] + amount,
                current[1] + (current[2] * amount),
                current[2],
            )

    return current[0] * current[1]


if __name__ == "__main__":
    directions = get_input()

    print(handle_commands_pt1(directions))
    print(handle_commands_pt2(directions))
