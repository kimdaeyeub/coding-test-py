def solution(N, stages):
    fail_rates = {}
    total_player = len(stages)

    for stage in range(1, N + 1):
        count = sum(1 for i in stages if i == stage)
        if total_player > 0:
            fail_rate = count / total_player
        else:
            fail_rate = 0

        fail_rates[stage] = fail_rate
        total_player -= count

    answer = sorted(fail_rates.keys(), key=lambda x: (-fail_rates[x], x))
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
print(solution(4, [4, 4, 4, 4, 4]))  # [4,1,2,3]
