def f(k, start, lst):
    if k > M:
        print(*lst)
    else:
        for i in range(start, N+1):
            f(k+1, i, lst + [i])

N, M = map(int, input().split())
f(1, 1, [])