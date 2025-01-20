from collections import deque


def solution(cards1, cards2, goal):

    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for x in goal:
        if cards1 and cards1[0] == x:
            cards1.popleft()
        elif cards2 and cards2[0] == x:
            cards2.popleft()
        else:
            return "No"

    return "Yes"


print(
    solution(
        ["i", "drink", "water"],
        ["want", "to"],
        ["i", "want", "to", "drink", "water"],
    )
)  # "Yes"
print(
    solution(
        ["i", "water", "drink"],
        ["want", "to"],
        ["i", "want", "to", "drink", "water"],
    )
)  # "No"
