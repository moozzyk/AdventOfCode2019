import sys
from intcode import Intcode


def problem1(program):
    input, output = [], []
    cpu = Intcode(program, input, output)
    cpu.run()
    block_tiles = 0
    for i in range(0, len(output), 3):
        if output[i + 2] == 2:
            block_tiles += 1
    print(block_tiles)


with open(sys.argv[1], "r") as f:
    program = list(map(lambda n: int(n), f.readline().split(",")))
    problem1(program)
