from itertools import product

with open("/home/roflzyo/AOC/2022/day09/data.txt", "r", encoding="utf-8") as data_file:
    data = [x.strip("\n") for x in data_file.readlines()]


def trace_path(data: list[str]) -> int:
    H = (0,0)
    T = (0,0)
    paths = [[0, 0]]
    for node in data:
        # import pdb; pdb.set_trace()
        match node.split(" "):
            case ["U", val]:
                H, T = move(paths, H, T, int(val), v_dir=1)
            case ["D", val]:
                H, T = move(paths, H, T, int(val),  v_dir=-1)
            case ["L", val]:
                H, T = move(paths, H, T, int(val), h_dir=-1)
            case ["R", val]:
                H, T =move(paths, H, T, int(val), h_dir=1)

    return paths                


def move(paths: list[list], h_pos: tuple[int], t_pos: list[int], steps: str, h_dir: int = 0, v_dir: int = 0,) -> tuple:
    offsets = [x for x in product([1, 0, -1], repeat=2)]
    hh, hv = h_pos
    th, tv = t_pos
    for step in range(steps):
        hh += h_dir
        hv += v_dir
        if not (th-hh, tv-hv) in offsets:
            if (v_dir and th != hh):
                # import pdb; pdb.set_trace()
                th += abs(v_dir) if th < hh else -abs(v_dir)
                tv += v_dir
            elif (h_dir and tv != hv):
                tv += abs(h_dir) if tv < hv else -abs(h_dir)
                th += h_dir
            else:
                th += h_dir
                tv += v_dir
        if [th, tv] not in paths:
            paths.append([th, tv])

    return ((hh, hv), (th, tv))


print(len(trace_path(data)))