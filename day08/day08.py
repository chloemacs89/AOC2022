from math import prod

with open("./data.txt", "r",
          encoding="utf-8") as data_file:
    data = [
        list(map(int, y))
        for y in [list(x.strip("\n")) for x in data_file.readlines()]
    ]
    data_transpose = list(map(list, zip(*data)))


def look_for_trees(data: list[int], t_data: list[int]) -> int:
    ok_trees = len(data) * len(t_data) - (len(data) - 2) * (len(t_data) - 2)
    offsets = (0, len(data) - 1, len(t_data) - 1)
    for ix, iy in enumerate(data):
        if ix not in offsets:
            for jx, jy in enumerate(iy):
                if jx not in offsets:
                    p_line, n_line, p_col, n_col = surrounding(data, t_data, iy, ix, jx)
                    ok_trees += check_tree(p_line, n_line, p_col, n_col, jy)

    return ok_trees


def look_for_views(data: list[data], t_data: list[int]) -> list[int]:
    views = []
    for ix, iy in enumerate(data):
        for jx, jy in enumerate(iy):
            surr = surrounding(data, t_data, iy, ix, jx)
            view = []
            # import pdb; pdb.set_trace()
            for v in surr:
                view.append(calc_view(v, jy))
            views.append(prod(view))

    return max(views)


def surrounding(data: list[int], t_data: list[int], curr_list: list[int], row: int, col: int) -> tuple:
    return (data[row][0:col][::-1], data[row][col+1: len(curr_list)], t_data[col][0:row][::-1], t_data[col][row+1:len(t_data[row])]) # NOQA


def check_tree(pl, nl, pc, nc, val) -> int:
    check = (
        bool(val > max(pl)),
        bool(val > max(nl)),
        bool(val > max(pc)),
        bool(val > max(nc)),
    )

    return 1 if any(check) else 0


def calc_view(values: list[int], val: int) -> int:
    if not values:
        return 0

    view = 0
    for x in values:
        view += 1
        if x >= val:
            return view

    return view


print(look_for_trees(data, data_transpose))
print(look_for_views(data, data_transpose))
