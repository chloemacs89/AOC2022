with open("./data.txt", "r", encoding="utf-8") as data_file:
    data = [x.strip("\n") for x in data_file.readlines()]

def program(data: list[str]) -> int:
    cycle = 0
    x = 1
    cycles = [(cycle, x)]
    crt = []
    row = ""
    for inst in data:
        # import pdb; pdb.set_trace()
        match inst.split(" "):
            case ["noop"]:
                row += draw(cycle, x-1)
                cycle += 1
                if not cycle % 40:
                    crt.append(row)                
                    row = ""
                cycles.append((cycle, x))
            case ["addx", val]:
                for _ in range(2):
                    row += draw(cycle, x-1)
                    cycle += 1
                    if not cycle % 40:
                        crt.append(row)                
                        row = ""
                    cycles.append((cycle, x))
                x += int(val)

    for r in crt:
        print(r)

    return sum([x[0]*x[1] for x in cycles if x[0] in range(20, 221, 40)])


def draw(cycle: int, x: int) -> str:
    return "#" if cycle%40 in range(x, x+3) else "."

print(program(data))