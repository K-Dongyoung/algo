import sys
sys.stdin = open('shelf.txt')

def dfs(k, s):
    global m
    if k == N:
        if s >= B:
            m = min(s, m)
    elif s >= m:
        return
    else:
        dfs(k+1, s+H[k])
        dfs(k+1, s)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    m = 200_000

    dfs(0, 0)

    print(f'#{tc} {m-B}')