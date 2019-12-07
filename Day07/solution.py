import sys
from itertools import permutations


def get_value(mode, program, address):
    if mode == 0:
        return program[program[address]]
    else:
        return program[address]


def run_program(program, input):
    ip = 0
    reg = input
    reg_idx = 0
    while ip < len(program):
        opcode = program[ip] % 100
        modes = program[ip] // 100
        if opcode == 1:
            program[program[ip + 3]] = get_value(modes % 10, program, ip + 1) \
                    + get_value(modes // 10, program, ip + 2)
            ip += 4
        elif opcode == 2:
            program[program[ip + 3]] = get_value(modes % 10, program, ip + 1) \
                    * get_value(modes // 10, program, ip + 2)
            ip += 4
        elif opcode == 3:
            program[program[ip + 1]] = reg[reg_idx]
            reg_idx = min(2, reg_idx + 1)
            ip += 2
        elif opcode == 4:
            reg[2] = get_value(modes % 10, program, ip + 1)
            ip += 2
        elif opcode == 5:
            if get_value(modes % 10, program, ip + 1) != 0:
                ip = get_value(modes // 10, program, ip + 2)
            else:
                ip += 3
        elif opcode == 6:
            if get_value(modes % 10, program, ip + 1) == 0:
                ip = get_value(modes // 10, program, ip + 2)
            else:
                ip += 3
        elif opcode == 7:
            if get_value(modes % 10, program, ip + 1) < \
                    get_value(modes // 10, program, ip + 2):
                program[program[ip + 3]] = 1
            else:
                program[program[ip + 3]] = 0
            ip += 4
        elif opcode == 8:
            if get_value(modes % 10, program, ip + 1) == \
                    get_value(modes // 10, program, ip + 2):
                program[program[ip + 3]] = 1
            else:
                program[program[ip + 3]] = 0
            ip += 4
        elif opcode == 99:
            return reg[2]


def calculate_thrust(program, phases):
    v = 0
    for phase in phases:
        v = run_program(list(program), [phase, v, 0])
    return v


def problem1(program):
    phases = [0, 1, 2, 3, 4]
    max_thrust = 0
    for subset in permutations(phases):
        max_thrust = max(max_thrust, calculate_thrust(program, subset))
    print(max_thrust)


with open(sys.argv[1], "r") as f:
    program = list(map(lambda n: int(n), f.readline().split(",")))
    problem1(program)
