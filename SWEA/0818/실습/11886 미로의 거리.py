import sys
sys.stdin = open('street_maze.txt')

from collections import deque

def path(S, E):
    Q = deque()
    Q.append((S, E))
    visited[S][E] = 1
    while Q:
        v = Q.popleft()
        for i in range(4):
            R = v[0] + di[i]
            C = v[1] + dj[i]
            if 0<=R<N and 0<=C<N:
                if maze[R][C] != 1 and visited[R][C] == 0:
                    Q.append((R, C))
                    visited[R][C] = visited[v[0]][v[1]] + 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                path(i, j)
                break

    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                ans = visited[i][j]
                break
    if ans > 0:
        ans -= 2

    print(f'#{tc} {ans}')