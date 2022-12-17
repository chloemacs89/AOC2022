import heapq as hq

heights = {x: e for e, x in enumerate("abcdefghijklmnopqrstuvwxyz")}
heights["S"] = 0
heights["E"] = 25

with open("/home/roflzyo/AOC/2022/day12/data.txt", "r",
          encoding="utf-8") as data_file:
    data = [list(y.strip("\n")) for y in data_file.readlines()]

start = [(x, y) for x, e in enumerate(data) for y, _ in enumerate(e)
         if _ == "S"][0]
stop = [(x, y) for x, e in enumerate(data) for y, _ in enumerate(e)
        if _ == "E"][0]


def check(a: int, b: int) -> bool:
    return True if b <= a + 1 else False


def dikjstra(data: list, start: tuple, stop: tuple, heights: dict):
    m = len(data)
    n = len(data[0])
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visited = [[False] * n for _ in range(m)]
    paths = [(0, start[0], start[1])]

    while True:
        step, x, y = hq.heappop(paths)

        if visited[x][y]:
            continue

        visited[x][y] = True

        if (x, y) == stop:
            return step

        for i, j in offsets:
            u = x + i
            w = y + j

            if not (0 <= u < m and 0 <= w < n):
                continue

            if check(heights[data[x][y]], heights[data[u][w]]):
                hq.heappush(paths, (step + 1, u, w))


def dikjstra2(data: list, start: tuple, stop: str, heights: dict):
    m = len(data)
    n = len(data[0])
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visited = [[False] * n for _ in range(m)]
    paths = [(0, start[0], start[1])]

    while True:
        step, x, y = hq.heappop(paths)

        if visited[x][y]:
            continue

        visited[x][y] = True

        if data[x][y] == stop:
            return step

        for i, j in offsets:
            u = x + i
            w = y + j

            if not (0 <= u < m and 0 <= w < n):
                continue

            if check(heights[data[u][w]], heights[data[x][y]]):
                hq.heappush(paths, (step + 1, u, w))


print(dikjstra(data, start, stop, heights))
print(dikjstra2(data, stop, "a", heights))
