import pprint as pp

heights: dict = {x:e for e, x in enumerate("abcdefghijklmnopqrstuvwxyz")}
heights["S"] = 0
heights["E"] = 25
INF = 1e7


with open("./test.txt", "r", encoding="utf-8") as data_file:
    data = [list(y.strip("\n")) for y in data_file.readlines()]


start = [(x, y) for x, e in enumerate(data) for y, _ in enumerate(e) if _ == "S"][0]
stop = [(x, y) for x, e in enumerate(data) for y, _ in enumerate(e) if _ == "E"][0]

nodes = [[(e, f) for f, _ in enumerate(x)] for e, x in enumerate(data)]
paths = {y:INF for x in nodes for y in x}
paths[start] = 0


def check(a: int, b: int) -> bool:
    return True if b <= a+1 else False


def find_path(paths: dict, nodes: list[tuple], data: list, heights: dict, pos: tuple, weight: int = 0):
    # breakpoint()
    print(pos)
    x, y = pos
    paths[pos] = weight
    offsets = [(x+i, y+n) for i, n in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    for n in offsets:
        i, j = n
        try:
            a = heights[data[x][y]]
            b = heights[data[i][j]]
            if check(a, b):
                w = weight + (b - a) if (b - a) == 1 else weight
                if paths[(i, j)] > weight:
                    find_path(paths, nodes, data, heights, n, w)
        except IndexError:
            pass
        except KeyError:
            pass

find_path(paths, nodes, data, heights, start)
pp.pp(paths)