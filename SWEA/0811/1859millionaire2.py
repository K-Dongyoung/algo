import sys
sys.stdin = open('millionaire.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_L = [0] * (N+1)
    max_L[-1] = arr[-1]
    profit = 0

    for i in range(N):
        if arr[N-1-i] > max_L[N - i]:
            max_L[N-1-i] = arr[N-1-i]
        else:
            max_L[N-1-i] = max_L[N-i]

    for i in range(N):
        if arr[i] < max_L[i]:
            profit += max_L[i] - arr[i]


    print(f'#{tc} {profit}')