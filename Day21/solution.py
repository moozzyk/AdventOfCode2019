import sys
from intcode import Intcode


def problem1(program):
    script = [
            "NOT A T",
            "NOT C J",
            "AND D J",
            "OR T J",
            "WALK",
            ]
    cpu = Intcode(program)
    for line in script:
        cpu.input.extend(list(map(ord, line + "\n")))

    cpu.run()
    print(cpu.output[-1])


with open(sys.argv[1], "r") as f:
    program = list(map(lambda n: int(n), f.readline().split(",")))
    problem1(program)
