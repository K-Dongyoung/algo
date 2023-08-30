import sys
sys.stdin = open('cart.txt')

def f(n, k):
    global min_sum
    sum_temp = 0
    if k == n:
        for i in range(len(p)-1):
            sum_temp += field[p[i]][p[i+1]]
        if min_sum > sum_temp:
            min_sum = sum_temp
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                p[k] = temp[i]
                f(n, k+1)
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    temp = [i for i in range(N)]
    p = [temp[0]] + [0] * (N-1) + [temp[0]]
    used = [0] * N
    used[0] = 1
    min_sum = 1000 * 1000
    f(N, 1)
    print(f'#{tc} {min_sum}')