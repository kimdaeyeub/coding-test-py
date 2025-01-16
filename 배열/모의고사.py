def solution(answers):
    arr = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    count = [0] * 3
    for i in range(len(answers)):
        for j in range(len(arr)):
            if answers[i] == arr[j][i % len(arr[j])]:
                count[j] += 1
    maxCount = max(count)
    answers = []
    for i in range(len(count)):
        if maxCount == count[i]:
            answers.append(i + 1)

    return answers


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
