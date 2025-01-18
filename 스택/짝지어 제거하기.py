def solution(s):
    answer = 0
    stack = []
    for i in list(s):
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution("baabaa"))  # 1
print(solution("cdcd"))  # 0
