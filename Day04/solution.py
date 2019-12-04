def has_consecutive(number):
    i = 1
    while i < len(number):
        if number[i] == number[i - 1]:
            return True
        i += 1
    return False


def recurse(min, max, number, digit):
    if (len(number) > len(max)):
        return 0

    count = 0
    if len(number) > 0 and number[0] != '0' and int(number) >= int(
            min) and int(number) <= int(max) and has_consecutive(number):
        count += 1
        print(number)

    for d in range(digit, 10):
        count += recurse(min, max, number + str(d), d)

    return count


def problem1(min, max):
    return recurse(str(min), str(max), "", 0)


print(problem1(137683, 596253))
