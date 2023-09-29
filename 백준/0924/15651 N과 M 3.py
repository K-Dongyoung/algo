def perm(n, m, k, lst):
    if k == m:
        print(*lst)
        return
    for i in range(1, N+1):
        perm(n, m, k+1, lst + [i])


N, M = map(int, input().split())
perm(N, M, 0, [])