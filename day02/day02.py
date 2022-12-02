d = {
    ("A", "X"): (1, 1, 3, 3),
    ("A", "Y"): (1, 2, 0, 6),
    ("A", "Z"): (1, 3, 6, 0),
    ("B", "X"): (2, 1, 6, 0),
    ("B", "Y"): (2, 2, 3, 3),
    ("B", "Z"): (2, 3, 0, 6),
    ("C", "X"): (3, 1, 0, 6),
    ("C", "Y"): (3, 2, 6, 0),
    ("C", "Z"): (3, 3, 3, 3),
}

d_case = {
    ("A", "X"): ("A", "Z"),
    ("A", "Y"): ("A", "X"),
    ("A", "Z"): ("A", "Y"),
    ("B", "X"): ("B", "X"),
    ("B", "Y"): ("B", "Y"),
    ("B", "Z"): ("B", "Z"),
    ("C", "X"): ("C", "Y"),
    ("C", "Y"): ("C", "Z"),
    ("C", "Z"): ("C", "X"),
}


points_first_case = {
    "myself": 0,
    "opponent": 0
}

points_second_case = {
    "myself": 0,
    "opponent": 0
}

def add_points(case, pattern, points):
    points["myself"] += pattern[case][1] + pattern[case][3]
    points["opponent"] += pattern[case][0] + pattern[case][2]


with open("./data.txt", "r", encoding="utf-8") as data_file:
    for x in data_file.readlines():
        case = tuple(x.strip(" \n").split(" "))
        add_points(case, d, points_first_case)
        add_points(d_case[case], d, points_second_case)

print(points_first_case["myself"])
print(points_second_case["myself"])