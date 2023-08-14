T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N):
        for j in range(M):
            sum_temp = arr[i][j]
            for ai, aj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                bi = i + ai
                bj = j + aj
                if 0 <= bi <N and 0<= bj < M:
                    sum_temp += arr[bi][bj]
            if max_sum < sum_temp:
                max_sum = sum_temp

    print(f'#{tc} {max_sum}')