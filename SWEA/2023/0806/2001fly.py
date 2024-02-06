import sys; sys.stdin = open('fly.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_f = 0
    for i in range(N-M+1):
        for j in range(N - M + 1):
            sum_f = 0
            for m in range(i, i+M):
                for n in range(j, j+M):
                    sum_f += arr[m][n]
            if max_f < sum_f:
                max_f = sum_f

    print(f'#{tc} {max_f}')