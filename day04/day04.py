with open("./data.txt", "r", encoding="utf-8") as data_file:
    solve1 = sum([1 for y in [x.strip("\n").replace("-", " ").replace(",", " ").split(" ") for x in data_file.readlines()] if (set(range(int(y[0]), int(y[1])+1)).issuperset(set(range(int(y[2]), int(y[3])+1))) or set(range(int(y[0]), int(y[1])+1)).issubset(set(range(int(y[2]), int(y[3])+1))))]) # NOQA

print(solve1)
