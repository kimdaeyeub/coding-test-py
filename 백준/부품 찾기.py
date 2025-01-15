N = 5
arr = [8, 3, 7, 9, 2]
arr.sort()

M = 3
data = [5, 7, 9]


def binary_search(target, start, end, arr):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return "yes"
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "no"


answer = ""
for i in range(len(data)):
    result = binary_search(data[i], 0, len(arr) - 1, arr)
    answer += result + " "

print(answer)
