import sys
sys.stdin = open('bus.txt')

def f(n, k, c):
    global min
    if k == n-1:
        if min > c-1:
            min = c-1
        return
    if c >= min:
        return
    else:
        for i in range(1, M[k]+1):
            if k+i >= n:
                break
            f(n, k+i, c+1)


T = int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    M = temp[1:]
    min = N
    f(N, 0, 0)
    print(f'#{tc} {min}')