from collections import deque
import re

with open("./data.txt", "r", encoding="utf-8") as data_file:
    data = data_file.read().split("\n\n")

crates = []

for x in list(zip(*data[0].split("\n"))):
    current_crates = deque((re.sub(r"\W+|\d", "", "".join(x))))
    if current_crates:
        crates.append(current_crates)

program = [
    tuple(map(int, y.lstrip().split(" ")))
    for y in [re.sub(r"\D+", " ", x) for x in data[1].rstrip().split("\n")]
]


# first star
def move_crates(program: list, crates: list[deque]):
    for n in program:
        for x in range(n[0]):
            crates[n[2] - 1].appendleft(crates[n[1] - 1].popleft())


move_crates(program, crates)
print("".join([x[0] for x in crates if x]))
