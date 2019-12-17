import sys
from intcode import Intcode


def create_map(program):
    cpu = Intcode(program)
    cpu.run()
    return list(filter(lambda l: l != "", "".join(list(map(lambda n: chr(n), cpu.output))).split("\n")))


def problem1(program):
    alignment_sum = 0
    view = create_map(program)
    for row in range(1, len(view) - 1):
        for col in range(1, len(view[row]) - 1):
            if view[row][col] == '#' and view[row - 1][col] == "#" and view[row + 1][col] == "#" and view[row][col - 1] == "#" and view[row][col + 1] == "#":
                alignment = row * col
                alignment_sum += alignment
    print(alignment_sum)

with open(sys.argv[1], "r") as f:
    program = list(map(lambda n: int(n), f.readline().split(",")))
    problem1(program)