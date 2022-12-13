def signal_strength(cycles, X):
    return cycles * X if cycles in range(20, 221, 40) and cycles <= 220 else 0


def get_idx(cycles):
    if cycles <= 40:
        return 0
    elif 40 < cycles <= 80:
        return 1
    elif 80 < cycles <= 120:
        return 2
    elif 120 < cycles <= 160:
        return 3
    elif 160 < cycles <= 200:
        return 4
    else:
        return 5


with open("input", "r") as f:

    X = 1
    cycles = 0
    res = 0
    sprite = range(3)
    grid = [["." for _ in range(40)] for _ in range(6)]
    for line in f:
        match line.split():
            case ["addx", val]:
                for _ in range(2):
                    cycles += 1
                    res += signal_strength(cycles, X)
                    if cycles % 40 in sprite:
                        print(get_idx(cycles))
                        grid[get_idx(cycles)][cycles % 40 - 1] = "#"
                X += int(val)
                sprite = range(X, X + 3)

            case ["noop"]:
                cycles += 1
                res += signal_strength(cycles, X)
                if cycles % 40 in sprite:
                    grid[get_idx(cycles)][cycles % 40 - 1] = "#"

for line in grid:
    print(line)


print(res)
