from collections import defaultdict

with open("input", "r") as f:
    inp = f.readlines()


fs = defaultdict(list)
sizes = defaultdict(int)

parent = {}
vals = defaultdict(int)
# final_sizes = defaultdict(int)

size_tracker = 0
for line in inp:
    cmds = line.split()
    if cmds[1] == "cd":

        if cmds[2] == "/":
            cwd = "/"

        if cmds[2] == "..":
            cwd = parent[cwd]
            for child in fs[cwd]:
                vals[cwd] += vals[child]
            size_tracker = 0
        else:
            if size_tracker == 0:
                cur_parent = cwd
                # size_tracker += 1
            else:
                size_tracker += 1

            parent[cmds[2]] = cur_parent
            # dir_stack.append(cmds[2])
            cwd = cmds[2]
    elif cmds[0] == "dir":
        fs[cwd].append(cmds[1])

    elif cmds[0].isnumeric():
        vals[cwd] += int(cmds[0])


print(vals)

print(sum(s for s in vals.values() if s <= 100000))
