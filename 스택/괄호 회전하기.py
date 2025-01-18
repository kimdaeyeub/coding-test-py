def solution(s):
    answer = 0
    list_data = list(s)
    for _ in range(len(list_data)):
        stack = []
        poped_data = list_data.pop(0)

        list_data.append(poped_data)
        for x in list_data:

            if len(stack) == 0:
                stack.append(x)
            elif x == "]" and stack[len(stack) - 1] == "[":
                stack.pop()
            elif x == "}" and stack[len(stack) - 1] == "{":
                stack.pop()
            elif x == ")" and stack[len(stack) - 1] == "(":
                stack.pop()
            else:
                stack.append(x)

        if len(stack) == 0:
            answer += 1

    return answer


print(solution("[](){}"))  # 3
print(solution("}]()[{"))  # 2
print(solution("[)(]"))  # 0
print(solution("}}}"))  # 0
