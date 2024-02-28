import sys
sys.stdin = open("input1.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N):
        for j in range(M):
            sum_temp = arr[i][j]
            for k in range(1, arr[i][j] + 1):
                for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    R = i + k * di
                    C = j + k * dj
                    if 0 <= R < N and 0 <= C < M:
                        sum_temp += arr[R][C]
            if sum_temp > max_sum:
                max_sum = sum_temp

    print(f"#{tc} {max_sum}")