import sys
sys.stdin = open('quad4.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = (i+1) * (j+1)

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
