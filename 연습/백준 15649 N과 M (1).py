def p(n, lst):
    if n == M:
        print(*lst)

    else:
        for i in range(1, N + 1):
            if v[i] == 0:
                v[i] = 1
                p(n + 1, lst + [i])
                v[i] = 0


N, M = map(int, input().split())
v = [0] * (N + 1)
p(0, [])
