values = {x:i+1 for i, x in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")} # NOQA

with open("./data.txt", "r", encoding="utf-8") as data_file:
    solve1 = sum([values.get(tuple(set(x[:int(len(x.strip("\n"))/2)]).intersection(set(x[int(len(x.strip("\n"))/2):])))[0], 0) for x in data_file.readlines()]) # NOQA

print(solve1)
