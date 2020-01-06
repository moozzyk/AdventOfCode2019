import sys


def find_keys(maze):
    keys = {}
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            tile = maze[row][col]
            if tile == "@" or (tile.isalpha() and tile.islower()):
                keys[tile] = (row, col)
    return keys


def get_path_to_key(start, end_key, maze):
    q = [(start, 0, 0, 0)]
    visited = set()
    while q:
        ((row, col), steps, required_keys, collected_keys) = q.pop(0)
        if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[row]) \
                or maze[row][col] == "#" or (row, col) in visited:
            continue
        visited.add((row, col))

        tile = maze[row][col]
        if tile.isalpha():
            key = 1 << (ord(tile.lower()) - ord("a"))
            if tile.islower():
                collected_keys |= key
            else:
                if collected_keys & key == 0:
                    required_keys |= key

        if tile == end_key:
            return ((row, col), steps, required_keys, collected_keys)

        for (d_row, d_col) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            q.append(((row + d_row, col + d_col), steps + 1, required_keys,
                     collected_keys))


def get_path_to_key_cached(start, end_key, maze, paths):
    start_key = maze[start[0]][start[1]]
    path_points = (start_key, end_key)
    if path_points not in paths.keys():
        paths[path_points] = get_path_to_key(start, end_key, maze)
    return paths[path_points]


def get_path(start, all_keys, maze):
    cached_paths = {}
    visited = {}
    q = [(start, 0, 0)]
    min_steps = 10000000
    while q:
        (pos, steps, collected_keys) = q.pop(0)
        if collected_keys == all_keys:
            min_steps = min(min_steps, steps)
            continue
        num_steps = visited.get((pos, collected_keys), 10000000)
        if steps >= num_steps:
            continue
        visited[(pos, collected_keys)] = steps

        for key in range(bin(all_keys).count("1")):
            if collected_keys & (1 << key) != 0:
                continue
            target_key = chr(ord("a") + key)
            (new_pos, seg_steps, req_keys, new_keys) = get_path_to_key_cached(
                    pos, target_key, maze, cached_paths)
            if collected_keys & req_keys == req_keys:
                q.append((new_pos, steps + seg_steps,
                         collected_keys | new_keys))

    return min_steps


def problem1(maze):
    keys = find_keys(maze)
    start = keys.pop("@")
    all_keys = 0
    for k in keys:
        all_keys |= 1 << (ord(k) - ord("a"))

    min_steps = get_path(start, all_keys, maze)
    print(min_steps)


with open(sys.argv[1], "r") as f:
    maze = f.read().splitlines()
    problem1(maze)
