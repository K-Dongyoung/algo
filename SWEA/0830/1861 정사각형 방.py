import sys
sys.stdin = open('square.txt')

def find(x):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == x:
                return i, j

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    r, c = find(1)
    start = 1
    cnt = 1
    temp = [0] * 2

    while True:
        if arr[r][c] == N**2:
            break
        flag = False
        for i in range(4):
            R = r + di[i]
            C = c + dj[i]
            if 0 <= R < N and 0 <= C < N and arr[R][C] == arr[r][c] + 1:
                r = R
                c = C
                cnt += 1
                flag = True
                break
        if not flag:
            if temp[1] < cnt:
                temp[0] = start
                temp[1] = cnt
            r, c = find(start + cnt)
            cnt = 1
            start =arr[r][c]
        if temp[1] < cnt:
            temp[0] = start
            temp[1] = cnt

    print(f'#{tc}', *temp)