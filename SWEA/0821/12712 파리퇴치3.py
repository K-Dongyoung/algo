import sys
sys.stdin = open('fly.txt')

def f(arr, N, M):
    max_fly = 0
    for i in range(N):
        for j in range(N):
            sum_temp1 = arr[i][j]
            sum_temp2 = arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    R1 = i + da[k] * m
                    C1 = j + db[k] * m
                    R2 = i + dc[k] * m
                    C2 = j + dd[k] * m
                    if 0<=R1<N and 0<=C1<N:
                        sum_temp1 += arr[R1][C1]
                    if 0<=R2<N and 0<=C2<N:
                        sum_temp2 += arr[R2][C2]
            if max_fly < sum_temp1:
                max_fly = sum_temp1
            if max_fly < sum_temp2:
                max_fly = sum_temp2
    return max_fly


da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

dc = [-1, 1, 1, -1]
dd = [1, 1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {f(arr, N, M)}')
