import sys
sys.stdin = open('min_cost.txt')

def dijkstra(r, c):
    D[r][c] = 0
    Q = [[r, c]]
    for i in range(N):
        for j in range(N):
            min_v = tmp
            idx = 0
            for k in range(len(Q)):
                if not visited[Q[k][0]][Q[k][1]] and D[Q[k][0]][Q[k][1]] < min_v:
                    min_v = D[Q[k][0]][Q[k][1]]
                    R = Q[k][0]
                    C = Q[k][1]
                    idx = k

            Q.pop(idx)
            visited[R][C] = 1
            if R == N-1 and C == N-1:
                return
            for w in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ar = R + w[0]
                ac = C + w[1]
                if 0 <= ar < N and 0 <= ac < N and not visited[ar][ac]:
                    if height[ar][ac] > height[R][C]:
                        if D[ar][ac] > D[R][C] + 1 + height[ar][ac] - height[R][C]:
                            D[ar][ac] = D[R][C] + 1 + height[ar][ac] - height[R][C]
                            Q.append([ar, ac])
                    else:
                        if D[ar][ac] > D[R][C] + 1:
                            D[ar][ac] = D[R][C] + 1
                            Q.append([ar, ac])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    tmp = 100 * 100 * 999 + 1
    visited = [[0] * N for _ in range(N)]
    D = [[tmp] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')