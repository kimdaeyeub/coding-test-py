#  2 <= N <= 100,000
#  2 <= K <= 100,000
N, K = map(int, input().split())
count = 0
while N != 1:
    if N % K == 0:
        N = N / K
    else:
        N -= 1
    count += 1

print(count)
