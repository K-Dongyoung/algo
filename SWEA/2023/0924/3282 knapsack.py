import sys
sys.stdin = open('knapsack.txt')

def dfs(k, cv, cc):
    global max_c
    if cv > K:
        return
    if k == N:
        return
    if cc > max_c:
        max_c = cc
    dfs(k+1, cv + arr[k][0], cc + arr[k][1])
    dfs(k+1, cv, cc)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = []
    for _ in range(N):
        v, c = map(int, input().split())
        arr.append((v, c))


    max_c = 0

    dfs(0, 0, 0)

    print(f'#{tc} {max_c}')