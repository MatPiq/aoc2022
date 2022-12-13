from collections import OrderedDict


with open("test_input.txt", "r") as f:

    monkeys = OrderedDict()

    for i, monkey in enumerate(f.read().split("\n\n")):
        new_monkey = {}
        for line in monkey.split("\n"):
            match line.strip().split():
                case ["Starting", "items:", *items]:
                    new_monkey["items"] = [int(n.replace(",", "")) for n in items]

                case ["Operation:", "new" , "=", t1, op, t2]:
                    new_monkey["operation"] = [t1, op, t2]
                    

                case ["Test:", "divisible", "by", n]:
                    new_monkey["test"] = int(n)

                case ["If", "true:", "throw", "to", "monkey", m]:
                    new_monkey["iftrue"] = int(m)

                case ["If", "false:", "throw", "to", "monkey", m]:
                    new_monkey["iffalse"] = int(m)

        monkeys[i] = new_monkey


for round in range(1):

    for monkey in monkeys:

        worrylvl = monkey["items"].

print(monkeys)
