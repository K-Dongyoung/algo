import sys
sys.stdin = open('street.txt')

from collections import deque

def f(S, G):
    visited = [0] * (V+1)
    Q = deque()
    Q.append(S)
    visited[S] = 1
    while Q:
        v = Q.popleft()
        for w in range(1, V+1):
            if adj[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    if visited[G] == 0:
        return 0
    return visited[G] - 1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1
        adj[j][i] = 1
    S, G = map(int, input().split())

    print(f'#{tc} {f(S, G)}')