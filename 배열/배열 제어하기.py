def solution(arr):
    unique = list(set(arr))
    unique.sort(reverse=True)
    return unique


print(solution([4, 2, 2, 1, 3, 4]))
