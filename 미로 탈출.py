from collections import deque

# n = 5
# m = 6

# graph = [
#     [1, 0, 1, 0, 1, 0],
#     [1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1],
# ]
n = 3
m = 3
graph = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1],
]

# 괴물이 있는 부분은 0
# 괴물이 없는 부분은 1

# answer=10

visited = [[False] * m for _ in range(n)]

d = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
]


def bfs():
    queue = deque([[0, 0, 1]])
    visited[0][0] = True
    maxCount = 1
    while len(queue) > 0:
        x, y, z = queue.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if nx == m - 1 and ny == n - 1:
                return z + 1
            if (
                nx >= 0
                and ny >= 0
                and nx < m
                and ny < n
                and visited[ny][nx] == False
                and graph[ny][nx] == 1
            ):
                queue.append([nx, ny, z + 1])


value = bfs()
print(value)
