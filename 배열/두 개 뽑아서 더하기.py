def solution(numbers):
    results = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            results.append(numbers[i] + numbers[j])
    results = sorted(set(results))
    return results


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
