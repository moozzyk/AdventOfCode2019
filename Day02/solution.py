def problem1(program):
    program[1] = 12
    program[2] = 2
    ip = 0
    while ip < len(program):
        if program[ip] == 1:
            program[program[ip + 3]] = program[program[ip + 1]] + program[program[ip + 2]]
        elif program[ip] == 2:
            program[program[ip + 3]] = program[program[ip + 1]] * program[program[ip + 2]]
        elif program[ip]:
            print(program)
            return program[0]
        ip += 4
    return -1


with open("input.txt", "r") as f:
    input = list(map(lambda n: int(n), f.readline().split(",")))
    print(problem1(input.copy()))
