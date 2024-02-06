import sys
sys.stdin = open('balloon.txt')

def f(row, col, arr):
    max_sum = 0
    for i in range(row):
        for j in range(col):
            sum_temp = arr[i][j]
            for k in range(1, arr[i][j]+1):
                for m, n in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    r = i + m*k
                    c = j + n*k
                    if 0<=r<row and 0<=c<col:
                        sum_temp += arr[r][c]
            if max_sum < sum_temp:
                max_sum = sum_temp
    return max_sum

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = f(N, M, arr)
    print(f'#{tc} {result}')
