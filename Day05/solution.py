def get_value(mode, program, address):
    if mode == 0:
        return program[program[address]]
    else:
        return program[address]


def run_program(program, input):
    ip = 0
    reg = input
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
            program[program[ip + 1]] = reg
            ip += 2
        elif opcode == 4:
            reg = get_value(modes % 10, program, ip + 1)
            ip += 2
        elif opcode == 99:
            return reg
        else:
            print("invalid opcode: " + opcode)


with open("input.txt", "r") as f:
    program = list(map(lambda n: int(n), f.readline().split(",")))
    print(run_program(program, 1))
