values = {x:i+1 for i, x in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")} # NOQA

with open("./data.txt", "r", encoding="utf-8") as data_file:
    rucksacks = [sacks.strip("\n") for sacks in data_file.readlines()]
    solve1 = sum([values.get(tuple(set(x[:int(len(x)/2)]).intersection(set(x[int(len(x)/2):])))[0], 0) for x in rucksacks]) # NOQA
    solve2 = sum([values.get(tuple(set.intersection(set(z[0]), set(z[1]), set(z[2])))[0], 0) for z in [[rucksacks[y], rucksacks[y+1], rucksacks[y+2]] for y in range(0, len(rucksacks), 3)]]) # NOQA

print(solve1)
print(solve2)
