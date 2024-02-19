import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            local_sum = 0
            for k in range(M):
                for l in range(M):
                    local_sum += arr[i+k][j+l]
            if local_sum > max_sum:
                max_sum = local_sum

    print(f"#{tc} {max_sum}")