def visible(i, j, grid, vis_grid):
    return grid[i][j] > min(
        [grid[i][j - 1], grid[i][j + 1], grid[i - 1][j], grid[i + 1][j]]
    )


with open("test_input", "r") as f:

    grid = [[int(c) for c in line.strip()] for line in f]
    vis_grid = []
    print(grid)
    vis = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            if visible(i, j, grid):
                print(f"Val {grid[i][j]} on position {i},{j} if visible")
                vis += 1

    # vis = 0
    # for i, line in f:
    #     line = line.strip()
    #     for i in range(1, len(line) - 1):
    print(2 * len(grid) + 2 * len(grid[0]) - 4)
    print(vis)
