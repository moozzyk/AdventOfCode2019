from intcode import Intcode
import sys


def get_new_position(position, next_move):
    x, y = position
    if next_move == 1:
        position = (x, y + 1)
    elif next_move == 2:
        position = (x, y - 1)
    elif next_move == 3:
        position = (x - 1, y)
    elif next_move == 4:
        position = (x + 1, y)
    else:
        assert("Invalid move: " + next_move)

    return position


def find_oxygen(program):
    elements = ['#', '.', 'O']
    queue = [([i], get_new_position((0, 0), i)) for i in range(1, 5)]
    visited = {(0, 0): '.'}
    while queue:
        (path, position) = queue.pop(0)
        if position in visited.keys():
            continue
        cpu = Intcode(list(program), list(path))
        cpu.run()
        result = cpu.output.pop()
        visited[position] = elements[result]
        if result == 0:
            continue
        if result == 2:
            return path

        for next_move in range(1, 5):
            new_path = list(path)
            new_path.append(next_move)
            new_position = get_new_position(position, next_move)
            queue.append((new_path, new_position))

    assert("Oxygen not found.")


def problem1(program):
    path = find_oxygen(program)
    print(len(path))


with open(sys.argv[1], "r") as f:
    program = list(map(lambda n: int(n), f.readline().split(",")))
    problem1(program)
