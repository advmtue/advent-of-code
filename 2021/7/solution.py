INPUT_FILE = "input"


def get_input():
    with open(INPUT_FILE) as f:
        return [int(x) for line in f.readlines() for x in line.split(",")]


def pt_two_consumption_calc(start, stop):
    delta = abs(start - stop)
    return int(delta * ((delta + 1) / 2))


def determine_fuel_cost(starts, cost_calculator):
    return min(
        sum(cost_calculator(num, i) for num in starts) for i in range(max(starts))
    )


print("Part #1:", determine_fuel_cost(get_input(), lambda x, y: abs(x - y)))
print("Part #2:", determine_fuel_cost(get_input(), pt_two_consumption_calc))
