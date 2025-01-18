def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for x in range(len(board)):
            item = board[x][i - 1]
            if item != 0:
                if stack and stack[-1] == item:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(item)
                board[x][i - 1] = 0
                break

    return answer * 2


print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
)  # 4

# 4 3 1 1 3 2 4
