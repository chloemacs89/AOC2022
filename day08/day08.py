with open("./data.txt", "r",
          encoding="utf-8") as data_file:
    data = [
        list(map(int, y))
        for y in [list(x.strip("\n")) for x in data_file.readlines()]
    ]
    data_transpose = list(map(list, zip(*data)))


def look_for_trees(data: list[int], t_data: list[int]):
    ok_trees = len(data) * len(t_data) - (len(data) - 2) * (len(t_data) - 2)
    offsets = (0, len(data) - 1, len(t_data) - 1)
    for ix, iy in enumerate(data):
        if ix not in offsets:
            for jx, jy in enumerate(iy):
                if jx not in offsets:
                    p_line = data[ix][0:jx]
                    n_line = data[ix][jx + 1:len(iy)]
                    p_col = t_data[jx][0:ix]
                    n_col = t_data[jx][ix + 1:len(t_data[jx])]
                    # import pdb; pdb.set_trace()
                    ok_trees += check_tree(p_line, n_line, p_col, n_col, jy)

    return ok_trees


def check_tree(pl, nl, pc, nc, val):
    check = (
        bool(val > max(pl)),
        bool(val > max(nl)),
        bool(val > max(pc)),
        bool(val > max(nc)),
    )

    return 1 if any(check) else 0


print(look_for_trees(data, data_transpose))
