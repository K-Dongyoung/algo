import sys
sys.stdin = open('maze2.txt')

from collections import deque

def find(arr, x):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == x:
                return i, j

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


T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    path(*find(maze, 2))
    i, j = find(maze, 3)
    ans = visited[i][j]
    if ans > 0:
        ans = 1

    print(f'#{tc} {ans}')