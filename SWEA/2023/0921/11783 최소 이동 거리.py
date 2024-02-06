import sys
sys.stdin = open('min_dist.txt')

def dijkstra(start):
    D[start] = 0
    for i in range(N+1):
        min_v = tmp + 1
        for j in range(N+1):
            if not visited[j] and D[j] < min_v:
                min_v = D[j]
                v = j

        visited[v] = 1

        for w in adj[v]:
            if not visited[w[0]]:
                if D[w[0]] > D[v] + w[1]:
                    D[w[0]] = D[v] + w[1]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())

    adj = [[] for _ in range(N+1)]

    visited = [0] * (N+1)

    tmp = 0

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))
        tmp += w

    D = [tmp+1] * (N + 1)

    dijkstra(0)
    print(f'#{tc} {D[N]}')