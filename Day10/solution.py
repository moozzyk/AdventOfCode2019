import copy
import sys


def block_line(map, from_row, from_col, d_y, d_x):
    found = False
    while True:
        from_row += d_y
        from_col += d_x
        if (from_row < 0 or from_col < 0 or from_row >= len(map) or from_col >= len(map[0])):
            break
        if found:
            map[from_row][from_col] = "$"
        if map[from_row][from_col] == "#":
            found = True    


def block(map, from_row, from_col):
    for d_y in range(-len(map), len(map)):
        for d_x in range(-len(map[from_row]), len(map[from_row])):
            if not(d_x == 0 and d_y == 0):
                block_line(map, from_row, from_col, d_y, d_x)
            

def get_num_visible(map, row, col):
    if map[row][col] != "#":
        return 0

    map = copy.deepcopy(map)
    map[row][col] = "*"
    for to_row in range(len(map)):
        for to_col in range(len(map[to_row])):
            if map[to_row][to_col] == "#":
                block(map, row, col)

    num_visible = 0
    for line in map:
        num_visible += line.count('#')
    return num_visible


def problem1(map):
    max_num_visible, r, c = 0, -1, -1
    for row in range(len(map)):
        for col in range(len(map[row])):
            num_visible = get_num_visible(map, row, col)
            if num_visible > max_num_visible:
                max_num_visible, r, c = num_visible, row, col

    print(max_num_visible, r, c)


with open(sys.argv[1], "r") as f:
    map = []
    for line in f.read().splitlines():
        map.append(list(line))
    problem1(map)
