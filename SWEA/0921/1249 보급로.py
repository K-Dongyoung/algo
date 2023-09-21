import sys
sys.stdin = open('supply.txt')
# sys.stdin = open('1.txt')

def dijkstra(r, c):
    D[r][c] = 0
    Q = [[r, c]]
    for _ in range(N):
        for _ in range(N):
            min_v = 90000
            for k in range(len(Q)):
                if not visited[Q[k][0]][Q[k][1]] and D[Q[k][0]][Q[k][1]] < min_v:
                    min_v = D[Q[k][0]][Q[k][1]]
                    R = Q[k][0]
                    C = Q[k][1]
                    idx = k

            Q.pop(idx)
            visited[R][C] = 1
            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ar = R + i
                ac = C + j
                if 0 <= ar < N and 0 <= ac < N:
                    if not visited[ar][ac] and D[ar][ac] > D[R][C] + adj[ar][ac]:
                        D[ar][ac] = D[R][C] + adj[ar][ac]
                        Q.append([ar, ac])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    adj = [list(map(int, input())) for _ in range(N)]
    # 누적 거리 배열
    D = [[90000] * (N) for _ in range(N)]
    # visited
    visited = [[0] * (N) for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')
