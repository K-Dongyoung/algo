def perm(N, M, k):
    if k == M:
        print(*p)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            p[k] = a[i]
            perm(N, M, k+1)
            visited[i] = 0
    pass


N, M = map(int, input().split())
a = list(range(1, N+1))
p = [0] * M
visited = [0] * N
perm(N, M, 0)