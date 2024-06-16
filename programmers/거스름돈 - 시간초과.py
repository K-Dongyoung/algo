def solution(n, money):
    global answer
    p(n, money, 0, [])
    return answer


def p(n, money, total, change_list):
    global answer
    if n == total:
        answer += 1
        return
    if total > n:
        return
    else:
        for i in range(len(money)):
            p(n, money[i:], total + money[i], change_list + [money[i]])


answer = 0
print(solution(5, [1, 2, 5]))
