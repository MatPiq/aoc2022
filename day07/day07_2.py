from collections import defaultdict

with open("input", "r") as f:
    inp = f.readlines()


cwd_stack = []
dir_size = defaultdict(int)
free = 70_000_000
unused = 30_000_000

cwd = "/"
total_size = 0
for line in inp:

    cmd = line.strip().split()

    if cmd[1] == "cd":

        if cmd[2] == "/":
            cwd_stack = []

        elif cmd[2] == "..":
            cwd_stack.pop()

        else:
            cwd_stack.append(cmd[2])

    elif cmd[0].isnumeric():
        s = int(cmd[0])
        dir_path = ""
        for dir in cwd_stack:
            dir_path += f"/{dir}"
            dir_size[dir_path] += s

        total_size += s

size_needed = 30_000_000 - (70_000_000 - total_size)
print(sum(d for d in dir_size.values() if d <= 100_000))
print(min(d for d in dir_size.values() if d >= size_needed))
