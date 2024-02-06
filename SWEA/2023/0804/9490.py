import sys; sys.stdin = open('balloon.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max = 0

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            for k in range(4):
                for m in range(1, arr[i][j]+1):
                    row = i + m*di[k]
                    col = j + m*dj[k]
                    if 0 <= row < N and 0 <= col < M:
                        sum += arr[row][col]
            if max < sum:
                max = sum

    print(f'#{tc} {max}')