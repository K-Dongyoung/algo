def p(n, lst, s):
    if n == M:
        print(*lst)

    else:
        for i in range(s, N + 1):
            p(n + 1, lst + [i], i + 1)


N, M = map(int, input().split())
p(0, [], 1)
