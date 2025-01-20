from math import ceil
from collections import deque


def solution(progresses, speeds):
    answer = []
    qp = deque(progresses)
    qs = deque(speeds)
    day = 0
    length = 0
    while len(qp) > 0 and len(qs) > 0:
        if qp[0] + day * qs[0] >= 100:
            qp.popleft()
            qs.popleft()
            length += 1
        else:
            day = ceil((100 - qp[0]) / qs[0])
            if length != 0:
                answer.append(length)
                length = 0

    if length != 0:
        answer.append(length)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))  # [2,1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1,3,2]
