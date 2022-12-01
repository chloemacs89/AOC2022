data = []

with open("./data.txt", "r", encoding="utf-8") as data_file:
    data = [
        sum(map(int, (x.split("\n"))))
        for x in data_file.read().rstrip("\n").split("\n\n")
    ]

# first star
print(max(data))

# second star
print(sum(sorted(data, reverse=True)[:3]))
