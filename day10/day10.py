with open("./data.txt", "r", encoding="utf-8") as data_file:
    data = [x.strip("\n") for x in data_file.readlines()]

def program(data: list[str]) -> int:
    cycle = 0
    x = 1
    cycles = [(cycle, x)]
    for inst in data:
        match inst.split(" "):
            case ["noop"]:
                cycle += 1
                cycles.append((cycle, x))
            case ["addx", val]:
                for _ in range(2):
                    cycle += 1
                    cycles.append((cycle, x))
                x += int(val)

    return sum([x[0]*x[1] for x in cycles if x[0] in range(20, 221, 40)])


print(program(data))