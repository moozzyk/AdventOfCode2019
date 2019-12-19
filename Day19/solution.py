import sys
from intcode import Intcode

def problem1(program):
    input_stream = []
    output_stream = []
    for x in range(0, 50):
        for y in range(0, 50):
            cpu = Intcode(program, input_stream, output_stream)
            cpu.input.append(x)
            cpu.input.append(y)
            cpu.run()
    print(output_stream.count(1))


with open(sys.argv[1], "r") as f:
    program = list(map(lambda n: int(n), f.readline().split(",")))
    problem1(program)