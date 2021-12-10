INFILE = "input"


def get_input():
    with open(INFILE) as f:
        return [x.strip() for x in f.readlines()]


def is_matching_bracket(o, c):
    if o == "[":
        return c == "]"
    elif o == "(":
        return c == ")"
    elif o == "<":
        return c == ">"
    elif o == "{":
        return c == "}"

    return False


def is_opening_bracket(b):
    return b in ["[", "(", "{", "<"]


def solution():
    inputs = get_input()

    points_p1 = {"]": 57, ")": 3, "}": 1197, ">": 25137}
    points_p2 = {"]": 2, ")": 1, "}": 3, ">": 4}
    matching_bracket = {"[": "]", "(": ")", "{": "}", "<": ">"}

    score_p1 = 0
    scores_p2 = []
    for line in inputs:
        stack = []
        line_is_corrupt = False
        for letter in line:
            if len(stack) == 0:
                # Will be an opening bracket
                stack.append(letter)
                continue

            current = stack.pop()
            if not is_matching_bracket(current, letter):
                if is_opening_bracket(letter):
                    stack.append(current)
                    stack.append(letter)
                    continue

                # corrupt
                score_p1 += points_p1[letter]
                line_is_corrupt = True
                break

            # closing bracket (do nothing)

        if line_is_corrupt:
            continue

        p2_score = 0
        while len(stack) != 0:
            o = stack.pop()
            p2_score = (p2_score * 5) + points_p2[matching_bracket[o]]

        scores_p2.append(p2_score)

    sorted_scores = sorted(scores_p2)
    score_p2 = sorted_scores[int(len(sorted_scores) / 2)]

    return score_p1, score_p2


print(solution())
