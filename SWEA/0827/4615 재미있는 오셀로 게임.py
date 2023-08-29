import sys
sys.stdin = open('Othello.txt')

def table():
    temp = [[0]*N for _ in range(N)]
    temp[N//2][N//2] = 2
    temp[N//2-1][N//2-1] = 2
    temp[N//2-1][N//2] = 1
    temp[N//2][N//2-1] = 1
    return temp

def play():
    for a in arr:
        r = a[0] - 1
        c = a[1] - 1
        arena[r][c] = a[2]
        for b in range(8):
            s = []
            nr = r + di[b]
            nc = c + dj[b]
            while 0<=nr<N and 0<=nc<N and arena[nr][nc] != 0 and arena[nr][nc] != a[2]:
                s.append((nr, nc))
                nr += di[b]
                nc += dj[b]
            if 0<=nr<N and 0<=nc<N and arena[nr][nc] == a[2]:
                for m, n in s:
                    arena[m][n] = a[2]
    cnt_black = 0
    cnt_white = 0
    for i in range(N):
        for j in range(N):
            if arena[i][j] == 1:
                cnt_black += 1
            if arena[i][j] == 2:
                cnt_white += 1

    return cnt_black, cnt_white

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    arena = table()
    print(f'#{tc}', *play())
