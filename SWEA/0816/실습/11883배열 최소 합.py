import sys
sys.stdin = open('min_sum.txt')

def f(k, N, sum):
    global min_sum
    if min_sum <= sum:
        return
    if k == N:
        if min_sum > sum:
            min_sum = sum

    else:
        for i in range(k, N):
            temp[k], temp[i] = temp[i], temp[k]
            f(k+1, N, sum + arr[k][temp[k]])
            temp[k], temp[i] = temp[i], temp[k]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = [i for i in range(N)]
    min_sum = 0
    for i in range(N):
        min_sum += arr[i][i]
    f(0, N, 0)
    print(f'#{tc} {min_sum}')