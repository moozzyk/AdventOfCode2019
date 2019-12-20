import sys

def find_portals(plan):
    portals = {}
    for row in range(len(plan)):
        for col in range(len(plan[row])):
            if plan[row][col] == ".":
                portal_id = ""
                if plan[row - 1][col].isupper():
                    portal_id = plan[row - 2][col] + plan[row - 1][col]
                if plan[row + 1][col].isupper():
                    portal_id = plan[row + 1][col] + plan[row + 2][col]
                if plan[row][col - 1].isupper():
                    portal_id = f"{plan[row][col - 2]}{plan[row][col - 1]}"
                if plan[row][col + 1].isupper():
                    portal_id = f"{plan[row][col + 1]}{plan[row][col + 2]}"

                if portal_id:
                    s = portals.get(portal_id, [])
                    s.append((row, col))
                    portals[portal_id] = s
    return portals


def shortest_path(start, end, plan, portals):
    queue = [(start, 0)]
    visited = set()
    while queue:
        (position, steps) = queue.pop(0)
        (row, col) = position
        if position in visited or plan[row][col] != ".":
            continue
        visited.add(position)
        if position == end:
            return steps
        queue.append(((row - 1, col), steps + 1))
        queue.append(((row + 1, col), steps + 1))
        queue.append(((row, col - 1), steps + 1))
        queue.append(((row, col + 1), steps + 1))
        portal_pos = portals.get((row, col), None)
        if portal_pos:
            queue.append((portal_pos, steps + 1))
    assert("Could not reach end")


def problem1(plan):
    portal_list = find_portals(plan)
    start = portal_list.pop("AA", None)[0]
    end = portal_list.pop("ZZ", None)[0]
    portals = {}
    for (p1, p2) in portal_list.values():
        portals[p1] = p2
        portals[p2] = p1

    steps = shortest_path(start, end, plan, portals)
    print(steps)

with open(sys.argv[1], "r") as f:
    problem1(f.readlines())