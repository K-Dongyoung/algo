import sys
sys.stdin = open('maze.txt')

def dfs(row, col):
    visited[row][col] = 1
    if arr[row][col] == 3:
        return
    for i in range(4):
        R = row + di[i]
        C = col + dj[i]
        if 0 <= R < N and 0 <= C < N:
            if (arr[R][C] == 0 or arr[R][C] == 3) and visited[R][C] == 0:
                dfs(R, C)

def find(x, N, arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == x:
                return i, j


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    row, col = find(2, N, arr)

    dfs(row, col)

    row, col = find(3, N, arr)

    print(f'#{tc} {visited[row][col]}')