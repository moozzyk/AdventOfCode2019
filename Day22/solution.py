import sys

DECK_SIZE = 10007

def problem1(operations):
    deck = list(range(DECK_SIZE))
    for op in operations:
        if op.startswith("cut"):
            n = int(op[4:])
            deck = deck[n:] + deck[:n]
        elif op.startswith("deal with"):
            n = int(op[20:])
            new_deck = [0] * DECK_SIZE
            target_pos = 0
            for i in range(DECK_SIZE):
                new_deck[target_pos] = deck[i]
                target_pos = (target_pos + n) % DECK_SIZE
            deck = new_deck
        elif op.startswith("deal into"):
            deck = deck[::-1]
            None
        else:
            assert("Unrecognized operation")
    print(deck.index(2019))


with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()
    problem1(lines)