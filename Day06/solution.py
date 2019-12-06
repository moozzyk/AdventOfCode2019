import sys


def build_orbits(lines):
    orbits = {}
    for l in lines:
        parts = l.split(")")
        orbits[parts[1]] = parts[0]
    return orbits


def path_length(start, obrbits):
    count = 0
    while start != "COM":
        start = orbits[start]
        count += 1
    return count


def problem1(orbits):
    total_orbits = 0
    for k in orbits.keys():
        total_orbits += path_length(k, orbits)
    print(total_orbits)


with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()
    orbits = build_orbits(lines)
    problem1(orbits)
