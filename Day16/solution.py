import sys


def run_phase(input, phase):
    pattern = [0, 1, 0, -1]
    out = []
    for idx in range(len(input)):
        pattern_idx = 0
        repeat_pattern = idx
        new_value = 0
        for digit in input:
            if repeat_pattern == 0:
                repeat_pattern = idx + 1
                pattern_idx = (pattern_idx + 1) % len(pattern)
            new_value += int(digit) * pattern[pattern_idx]
            repeat_pattern -= 1
        out.append(str(abs(new_value) % 10))
    return "".join(out)


def problem1(input_seq):
    for phase in range(1, 101):
        input_seq = run_phase(input_seq, phase)
    print("".join(input_seq)[:8])


with open(sys.argv[1], "r") as f:
    line = f.read().splitlines()[0]
    problem1(line)
