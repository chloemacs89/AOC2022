# monkeys = {
#     0: [[79, 98], ("mul", 19), (23, 2, 3), 0],
#     1: [[54, 65, 75, 74], ("add", 6), (19, 2, 0), 0],
#     2: [[79, 60, 97], ("self"), (13, 1, 3), 0],
#     3: [[74], ("add", 3), (17, 0, 1), 0]
# }

monkeys = {
    0: [[99, 63, 76, 93, 54, 73], ("mul", 11), (2, 7, 1), 0],
    1: [[91, 60, 97, 54], ("add", 1), (17, 3, 2), 0],
    2: [[65], ("add", 7), (7, 6, 5), 0],
    3: [[84, 55], ("add", 3), (11, 2, 6), 0],
    4: [[86, 63, 79, 54, 83], ("self"), (19, 7, 0), 0],
    5: [[96, 67, 56, 95, 64, 69, 96], ("add", 4), (5, 4, 0), 0],
    6: [[66, 94, 70, 93, 72, 67, 88, 51], ("mul", 5), (13, 4, 5), 0],
    7: [[59, 59, 74], ("add", 8), (3, 1, 3), 0],
}

def game(monkeys: dict):
    # import pdb; pdb.set_trace()
    for _ in range(20):
        for key, val in monkeys.items():
            if val[0]:
                while val[0]:
                    val[3] += 1
                    match val[1]:
                        case ("mul", nb):
                            val[0][0] = int(val[0][0]*nb/3)
                        case ("add", nb):
                            val[0][0] = int((val[0][0]+nb)/3)
                        case ("self"):
                            val[0][0] = int(val[0][0]*val[0][0]/3)
                    if not val[0][0] % val[2][0]:
                        monkeys[val[2][1]][0].append(val[0][0])
                    else:
                        monkeys[val[2][2]][0].append(val[0][0])
                    del val[0][0]

    activity = sorted([x[3] for x in monkeys.values()], reverse=True)
    return activity[0]*activity[1]


print(game(monkeys))