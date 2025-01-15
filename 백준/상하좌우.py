n = int(input())
data = list(input().split())

start = [1, 1]

d = {"R": [1, 0], "L": [-1, 0], "D": [0, 1], "U": [0, -1]}


for i in range(len(data)):
    x, y = start
    dx, dy = d[data[i]]
    nx = x + dx
    ny = y + dy
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    start = [nx, ny]


print(start)
