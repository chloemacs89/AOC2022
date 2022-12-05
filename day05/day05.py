from collections import deque
from copy import deepcopy
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
def move_crates_1(program: list, crates: list[deque]):
    new_crates = deepcopy(crates)
    for n in program:
        for x in range(n[0]):
            new_crates[n[2] - 1].appendleft(new_crates[n[1] - 1].popleft())

    return new_crates

# second star
def move_crates_2(program: list, crates: list[deque]):
    new_crates = deepcopy(crates)
    for n in program:
        for elem in list(new_crates[n[1]-1])[:n[0]][::-1]:
            new_crates[n[2]-1].appendleft(elem)
        for x in range(n[0]):
            new_crates[n[1]-1].popleft()

    return new_crates


first_star_crates = move_crates_1(program, crates)
print("".join([x[0] for x in first_star_crates if x]))

second_star_crates = move_crates_2(program, crates)
print("".join([x[0] for x in second_star_crates if x]))
