def solution(n, money):
    global answer
    p(n, money, 0)
    return answer


def p(n, money, total):
    global answer
    if n == total:
        answer += 1
        return
    if total > n:
        return
    else:
        for i in range(len(money)):
            p(n, money[i:], total + money[i])


answer = 0
print(solution(5, [1, 2, 5]))
