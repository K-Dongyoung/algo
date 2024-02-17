import sys
sys.stdin = open('balloon2.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for i in range(N):
        for j in range(M):
            temp_sum = arr[i][j]
            for k in range(4):
                ri = i + di[k]
                rj = j + dj[k]
                if 0 <= ri < N and 0 <= rj < M:
                    temp_sum += arr[ri][rj]
            if temp_sum > max_sum:
                max_sum = temp_sum

    print(f"#{tc} {max_sum}")

    """
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N):
        for j in range(M):
            temp_sum = arr[i][j]
            for k in range(4):
                I = i + di[k]
                J = j + dj[k]
                if 0 <= I < N and 0 <= J < M:
                    temp_sum += arr[I][J]
            if max_sum < temp_sum:
                max_sum = temp_sum

    print(f'#{tc} {max_sum}')
    """