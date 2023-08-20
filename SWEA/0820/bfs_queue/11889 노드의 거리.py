import sys
sys.stdin = open('dist.txt')


def f(S, G, adj, V):
    visited = [0] * (V+1)
    Q = [0] * V
    front = -1
    rear = -1
    rear += 1
    Q[rear] = S
    visited[S] = 1
    while front != rear:
        front += 1
        v = Q[front]
        if v == G:
            return visited[v] - 1
        for i in adj[v]:
            if visited[i] == 0:
                rear += 1
                Q[rear] = i
                visited[i] = visited[v] + 1
    return 0



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)
    S, G = map(int, input().split())
    print(f'#{tc} {f(S, G, adj, V)}')
