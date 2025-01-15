N = 4
M = 6
arr = [19, 15, 10, 17]


def binary_search(target, start, end, arr):
    while start <= end:
        mid = (start + end) // 2
        value = 0
        for i in arr:
            if mid >= i:
                continue
            else:
                value += i - mid

        if value == target:
            return mid
        elif value > target:
            start = mid + 1
        else:
            end = mid - 1


result = binary_search(M, 0, max(arr), arr)
print(result)
