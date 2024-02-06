T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    total_sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                I = i + di[k]
                J = j + dj[k]
                if 0 <= I <N and 0 <= J < N:
                    total_sum += abs(arr[i][j] - arr[I][J])

    print(f'#{tc} {total_sum}')