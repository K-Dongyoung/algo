import sys
sys.stdin = open('work.txt')

def perm(n, k, m):
    global max
    if k == n:
        if m > max:
            max = m
        return
    if m <= max:
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                perm(n, k+1, m * (arr[k][i])/100)
                visited[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [0] * N
    visited = [0] * N
    max = 0
    perm(N, 0, 1)
    max *= 100
    print(f'#{tc} {max:.6f}')