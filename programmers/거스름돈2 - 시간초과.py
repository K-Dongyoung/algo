def solution(n, money):
    m = [set() for _ in range(n + 1)]
    money.sort()

    for i in range(1, n + 1):
        f(i, money, m)

    return len(m[n])


def f(n, money, m):
    if n < money[0]:
        return
    for coin in money:
        if n < coin:
            break
        if n == coin:
            m[n].add((coin,))
        if m[n - coin]:
            for a in m[n - coin]:
                b = list(a)
                c = b + [coin]
                c.sort()
                c = tuple(c)
                m[n].add(c)


print(solution(5, [1, 2, 5]))
