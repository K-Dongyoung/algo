import sys
sys.stdin = open('min_cost.txt')

import heapq


def dijkstra(r, c):
    D[r][c] = 0
    for i in range(N):
        for j in range(N):
            min_v = tmp
            for k in range(N):
                for l in range(N):
                    if not visited[k][l] and D[k][l] < min_v:
                        min_v = D[k][l]
                        R = k
                        C = l
            visited[R][C] = 1
            for w in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ar = R + w[0]
                ac = C + w[1]
                if 0 <= ar < N and 0 <= ac < N and not visited[ar][ac]:
                    if height[ar][ac] > height[R][C]:
                        if D[ar][ac] > D[R][C] + 1 + height[ar][ac] - height[R][C]:
                            D[ar][ac] = D[R][C] + 1 + height[ar][ac] - height[R][C]
                    else:
                        if D[ar][ac] > D[R][C] + 1:
                            D[ar][ac] = D[R][C] + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    tmp = 100 * 100 * 999 + 1
    visited = [[0] * N for _ in range(N)]
    D = [[tmp] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')