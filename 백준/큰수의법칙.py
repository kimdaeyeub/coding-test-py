n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

a = max(arr)
arr.remove(a)

b = max(arr)
arr.remove(b)

sumA = (m - m % k) * a
sumB = (m % k) * b

print(sumA + sumB)
