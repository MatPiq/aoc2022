def is_reachable(x1, x2, y1, y2):
    if abs(x1 - x2) <= 1 or abs(y1 - y2) <= 1:
        return True
    else:
        return False


with open("test_input", "r") as f:

    tail = [(4, 0)]
    y = 4
    x = 0
    prev_dir = None

    for line in f:
        direction, steps = line.split()
        steps = int(steps)
        direction = direction.strip()
        xt, yt = x, y

        for _ in range(steps):
            if direction == "D":
                y += 1
            elif direction == "L":
                x -= 1
            elif direction == "R":
                x += 1
            elif direction == "U":
                y -= 1

            if not is_reachable(x, xt, y, yt):
                tail.append((yt, xt))


        # prev_direction = direction

grid = [["." for _ in range(6)] for _ in range(5)]

print(tail)

for y, x in set(tail):
    grid[y][x] = "#"

for l in grid:
    print(l)

print(len(set(tail)))
