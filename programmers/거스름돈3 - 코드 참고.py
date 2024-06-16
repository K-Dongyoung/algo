# 다른 코드 참고..
def solution(n, money):
    m = [1] + [0] * n
    for coin in money:
        for p in range(coin, n + 1):
            m[p] += m[p - coin]
    return m[n] % 1_000_000_007


print(solution(5, [1, 2, 5]))
