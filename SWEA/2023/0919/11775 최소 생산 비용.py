import sys
sys.stdin = open('min.txt')

def perm(n, k, s):
    global min
    if k == n:
        if s < min:
            min = s
        return
    if s >= min:
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                perm(n, k+1, s + arr[k][i])
                visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min = 0
    for i in range(N):
        min += arr[i][i]
    perm(N, 0, 0)
    print(f'#{tc} {min}')