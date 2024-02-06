import sys
sys.stdin = open('cart.txt')

def f(n, k, s):
    global min_sum
    sum_temp = 0
    if k == n:
        s += field[p[N-1]][p[N]]
        min_sum = min(min_sum, s)
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                p[k] = temp[i]
                if k>0 and s+field[p[k-1]][p[k]] < min_sum:
                    f(n, k+1, s+field[p[k-1]][p[k]])
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
    f(N, 1, 0)
    print(f'#{tc} {min_sum}')