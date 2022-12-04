with open("input", "r") as f:

    s = 0
    s2 = 0
    for line in f:
        a, b = line.strip().split(",")

        def get_set(r):
            l, h = map(int, r.split("-"))
            return set(range(l, h + 1))

        a = get_set(a)
        b = get_set(b)

        if len(a) > len(b) and b.issubset(a) or len(a) <= len(b) and a.issubset(b):
            s += 1

        if a.intersection(b) != set():
            print(a)
            print(b)
            s2 += 1
    print(s)
    print(s2)
