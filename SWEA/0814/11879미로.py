import sys
sys.stdin = open('maze.txt')

def dfs(row, col):
    visited[row][col] = 1   #방문체크
    if arr[row][col] == 2:  #2 만나면 return
        return
    for i in range(4):
        R = row + di[i]     #델타 인덱스
        C = col + dj[i]
        if 0 <= R < N and 0 <= C < N:   #인덱스 체크
            if (arr[R][C] == 0 or arr[R][C] == 2) and visited[R][C] == 0:
                dfs(R, C)    #방문, dfs

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    row = 0
    col = 0
    for a in range(len(arr[0])):
        if arr[0][a] == 3:
            col = a
            break

    dfs(0, col)

    for a in range(len(arr[0])):
        if arr[N - 1][a] == 2:
            col = a
            break

    print(f'#{tc} {visited[N - 1][col]}')