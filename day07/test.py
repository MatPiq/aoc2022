dir_sizes = dict()
dir_stack = list()
total_size = 0
with open('input') as f:
    for line in f:
        match line.strip().split():
            case ['$', 'cd', '/']:
                dir_stack = list()
            case ['$', 'cd', '..']:
                dir_stack.pop()
            case ['$', 'cd', dir_name]:
                dir_stack.append(dir_name)
            case ['$', 'ls']:
                pass
            case ['dir', dir_name]:
                pass
            case [size, file_name]:
                dir_path = ''
                for dir_name in dir_stack:
                    dir_path += '/' + dir_name
                    dir_sizes[dir_path] = dir_sizes.get(dir_path, 0) + int(size)
                total_size += int(size)
size_needed = 30_000_000 - (70_000_000 - total_size)
print('Day 7, part 1:', sum([size for size in dir_sizes.values() if size <= 100_000]))
#print('Day 7, part 2:', min([size for size in dir_sizes.values() if size >= size_needed]))
