import sys


def next_turn(bugs, row, col):
    num_bugs = 0
    num_bugs += 1 if row > 0 and bugs[row - 1][col] == '#' else 0
    num_bugs += 1 if row < len(bugs) - 1 and bugs[row + 1][col] == '#' else 0
    num_bugs += 1 if col > 0 and bugs[row][col - 1] == '#' else 0
    num_bugs += 1 if col < len(bugs[row]) - 1 and bugs[row][col + 1] == "#" else 0

    if bugs[row][col] == "#" and num_bugs != 1:
        return "."
    if bugs[row][col] == "." and (num_bugs == 1 or num_bugs == 2):
        return "#"
    return bugs[row][col]


def transform(bugs):
    new_bugs = [[] for i in range(len(bugs))]
    for row in range(len(bugs)):
        for col in range(len(bugs[row])):
            new_bugs[row].append(next_turn(bugs, row, col))
    return new_bugs


def calculate_biodiversity(bugs):
    power = 1
    biodiversity = 0
    for row in bugs:
        for field in row:
            biodiversity += power if field == "#" else 0
            power *= 2
    return biodiversity

def problem1(bugs):
    seen = set([calculate_biodiversity(bugs)])

    while True:
        bugs = transform(bugs)
        biodiversity = calculate_biodiversity(bugs)
        if biodiversity in seen:
            print(biodiversity)
            return
        seen.add(biodiversity)


with open(sys.argv[1], "r") as f:
    bugs = f.read().splitlines()
    problem1(bugs)