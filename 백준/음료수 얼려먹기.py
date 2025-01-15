n = 4
m = 5

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

visited = [[False] * m for _ in range(n)]

directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
]


def dfs(graph, i, j, visited):
    visited[i][j] = True
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and graph[ni][nj] == 0:
            dfs(graph, ni, nj, visited)


count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 0:
            dfs(graph, i, j, visited)
            count += 1

print(count)
