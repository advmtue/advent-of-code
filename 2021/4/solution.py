INPUT_FILE = "input"

from more_itertools import chunked

import numpy as np


def get_input():
    with open(INPUT_FILE) as f:
        calls = [int(x) for x in f.readline().strip().split(",")]

        remaining_lines = [
            [int(x) for x in line.strip().split()]
            for line in f.readlines()
            if line != "\n"
        ]

        boards = list(chunked(remaining_lines, 5))

    return calls, boards


def update_board(board, num):
    for (y, row) in enumerate(board):
        for (x, column) in enumerate(row):
            if column == num:
                board[y][x] = "X"
                return board

    return board


def board_wins(board):
    def board_has_full_row(b):
        for row in b:
            if len([x for x in row if x != "X"]) == 0:
                return True

    # Check horizontal
    if board_has_full_row(board):
        return True

    # Check vertical
    if board_has_full_row(np.transpose(board)):
        return True

    return False


def get_score(board):
    return sum(x for row in board for x in row if x != "X")


def pt_one():
    call_order, boards = get_input()

    for n in call_order:
        for (i, board) in enumerate(boards):
            boards[i] = update_board(board, n)

            if board_wins(board):
                return get_score(board) * n


def pt_two():
    call_order, boards = get_input()
    marked_boards = [[False, board] for board in boards]

    for n in call_order:
        for (i, board) in enumerate(marked_boards):
            if board[0]:
                continue

            marked_boards[i][1] = update_board(board[1], n)

            if board_wins(board[1]):
                board[0] = True

                # If all boards have won, this is the last board
                if len([b for b in marked_boards if not b[0]]) == 0:
                    return get_score(board[1]) * n


if __name__ == "__main__":
    print(pt_one())
    print(pt_two())
