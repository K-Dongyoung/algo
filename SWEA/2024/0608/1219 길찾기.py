import sys

sys.stdin = open("input.txt")


def dfs(v):
    visited[v] = 1

    for w in adj[v]:
        if visited[w] == 0:
            dfs(w)


T = 10
for tc in range(1, T + 1):
    a, edge = map(int, input().split())
    arr = list(map(int, input().split()))

    adj = [[] for _ in range(100)]
    for i in range(edge):
        s, e = arr[2 * i], arr[2 * i + 1]
        adj[s].append(e)

    visited = [0] * 100
    dfs(0)

    print(f"#{tc} {visited[99]}")
