recieve = int(input())


def solution(N):
    money = N
    count = 0
    while money > 0:
        if money >= 500:
            count += money // 500
            money = money % 500
        elif money >= 100:
            count += money // 100
            money = money % 100
        elif money >= 50:
            count += money // 50
            money = money % 50
        elif money >= 10:
            count += money // 10
            money = money // 10
        else:
            break
    return count


result = solution(recieve)
print(result)
