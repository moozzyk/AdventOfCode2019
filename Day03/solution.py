def split_path(raw_path):
    return map(lambda s: (s[0], int(s[1:])), raw_path.split(','))


def path_to_points(path):
    points = []
    x, y = 0, 0
    for segment in path:
        dir, length = segment
        d_x, d_y = 0, 0
        if dir == 'R':
            d_x = 1
        elif dir == 'L':
            d_x = -1
        elif dir == 'U':
            d_y = -1
        elif dir == 'D':
            d_y = 1

        for s in range(length):
            x += d_x
            y += d_y
            points.append((x, y))

    return points    


def problem1(path1, path2):
    point_set = set(path_to_points(path1))
    points = path_to_points(path2)
    min_dist = 1000000
    for p in reversed(points):
        if p in point_set:
            min_dist = min(min_dist, abs(p[0]) + abs(p[1]))
    return min_dist


with open("input.txt", "r") as f:
    path1 = split_path(f.readline())
    path2 = split_path(f.readline())
    print(problem1(path1, path2))
    # print(path_to_points(path1))
    # print(list(path1))
