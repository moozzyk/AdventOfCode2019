def calculate_energy(values):
    result = []
    for v in values:
        r = 0
        for i in v:
            r += abs(i)
        result.append(r)
    return result


def update_velocity(moons, velocities):
    coordinate = 0
    while coordinate < 3:
        for idx1 in range(len(moons)):
            for idx2 in range(len(moons)):
                if moons[idx1][coordinate] > moons[idx2][coordinate]:
                    velocities[idx1][coordinate] -= 1
                elif moons[idx1][coordinate] < moons[idx2][coordinate]:
                    velocities[idx1][coordinate] += 1
        coordinate += 1

    for m in range(len(moons)):
        for c in range(3):
            moons[m][c] += velocities[m][c]


def problem1(moons):
    velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for _ in range(1000):
        update_velocity(moons, velocities)
        print(moons, velocities)

    pot = calculate_energy(moons)
    kin = calculate_energy(velocities)
    total = 0
    for i in range(len(pot)):
        total += pot[i] * kin[i]
    print(total)


moons = [[17, -7, -11], [1, 4, -1], [6, -2, -6], [19, 11, 9]]
problem1(list(moons))
