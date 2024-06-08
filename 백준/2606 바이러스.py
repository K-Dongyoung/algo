def dfs(v, count):
    visited[v] = 1
    for w in range(1, N + 1):
        if adj[v][w] == 1 and visited[w] == 0:
            count = dfs(w, count + 1)
    return count


N = int(input())
M = int(input())
adj = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1


ans = dfs(1, 0)
print(ans)
