from collections import deque
import re

with open("./test.txt", "r", encoding="utf-8") as data_file:
    data = data_file.read().split("\n\n")

crates = deque()

for x in list(zip(*data[0].replace(" ", "-").split("\n"))):
    current_crates = list(re.sub(r"\W+|\d", "", "".join(x)))
    if current_crates:
        crates.append(current_crates)

program = [tuple(map(int, list(y))) for y in [re.sub(r"\D", "", x) for x in data[1].split("\n")]]

def move_crates(program, crates):
    pass