n, m = map(int, input().split())

value = -1

for _ in range(n):
    data = list(map(int, input().split()))
    if value < min(data):
        value = min(data)

print(value)
