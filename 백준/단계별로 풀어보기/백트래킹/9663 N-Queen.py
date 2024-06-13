dc = [-1, 0, 1]
def visit(r, c, v):
    visited[r][c] += v
    for i in range(3):
        R = r + 1
        C = c + dc[i]
        while 0<=R<N and 0<=C<N:
            visited[R][C] += v
            R += 1
            C += dc[i]

def dfs(k):
    global cnt
    if k == N:
        cnt += 1
        return
    for i in range(N):
        if visited[k][i] == 0:
            visit(k, i, 1)
            dfs(k+1)
            visit(k, i, -1)


N = int(input())
visited = [[0]*N for _ in range(N)]
cnt = 0
dfs(0)
print(cnt)
