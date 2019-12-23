import sys
from intcode import Intcode

def problem1(program):
    network = [Intcode(program, input_queue=[i], output_queue=[]) for i in range(50)]
    while True:
        for i in range(len(network)):
            cpu = network[i]
            if not cpu.input:
                cpu.input.append(-1)
            cpu.run()
            while cpu.output:
                address = cpu.output.pop(0)
                x = cpu.output.pop(0)
                y = cpu.output.pop(0)
                if address == 255:
                    print(y)
                    return
                network[address].input.extend([x, y])


with open(sys.argv[1], "r") as f:
    program = list(map(lambda n: int(n), f.readline().split(",")))
    problem1(program)