import sys
sys.stdin = open('min_sum.txt')

def dfs(r, c, sum):
    global min_sum
    if r == N - 1 and c == N - 1:
        if min_sum > sum:
            min_sum = sum
    if sum >= min_sum:
        return
    for i in range(2):
        R = r + di[i]
        C = c + dj[i]
        if R < N and C < N:
            dfs(R, C, sum+arr[R][C])

di = [1, 0]
dj = [0, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1000 * 1000
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {min_sum}')
