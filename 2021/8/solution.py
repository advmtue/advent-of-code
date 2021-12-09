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


# Candidate for the worst code I've ever written
def pt_two():
    inputs = get_input()
    totals = []
    for line in inputs:
        words = set(["".join(sorted(x)) for x in line[0].split(" ")])

        solved_words = {}

        # Solve the unique cases
        for word in words:
            if len(word) == 2:
                solved_words[1] = word
            elif len(word) == 3:
                solved_words[7] = word
            elif len(word) == 4:
                solved_words[4] = word
            elif len(word) == 7:
                solved_words[8] = word

        # Game logic:

        # The number 3 can be found by looking for a word with 3 remaining chars after [1] is removed
        # Search for 3
        for word in words:
            if len(set(word) - set(solved_words[1])) == 3:
                solved_words[3] = word
                break

        # 2
        # Remove [3] from each word, see how many letters remain.
        # If 1, the number can be 2, 4, 5, 9. Ignore 4.
        # If 2, the number can be 0, 6, 8. Ignore 8.
        for word in words:
            if word == solved_words[4] or word == solved_words[8]:
                continue

            diff_3 = set(word) - set(solved_words[3])
            if len(diff_3) == 1:
                if len(diff_3 - set(solved_words[4])) == 1:
                    solved_words[2] = word
                else:
                    # 5 or 9. Intersect with [1] and see what len remains
                    if len(set(word).intersection(solved_words[1])) == 2:
                        solved_words[9] = word
                    else:
                        solved_words[5] = word
            elif len(diff_3) == 2:
                if len(set(word).intersection(solved_words[1])) == 1:
                    solved_words[6] = word
                else:
                    solved_words[0] = word

        num = ""
        for word in ["".join(sorted(w)) for w in line[1].split(" ")]:
            for isolved_word in solved_words:
                if solved_words[isolved_word] == word:
                    num += str(isolved_word)

        totals.append(num)

    return sum(int(x) for x in totals)


print("Part #1:", pt_one())
print("Part #2:", pt_two())
