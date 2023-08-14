import sys
sys.stdin = open('balloon.txt')

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_f = 0
    for i in range(N):
        for j in range(M):
            sum_f = arr[i][j]
            for k in range(4):
                I = i + di[k]
                J = j + dj[k]
                if 0 <= I < N and 0 <= J < M:
                    sum_f += arr[I][J]
            if max_f < sum_f:
                max_f = sum_f

    print(f'#{tc} {max_f}')
