import sys
sys.stdin = open('circular1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    circular = ''

    for i in range(N):
        for j in range(N-M+1):
            OX = True
            for k in range(M//2):
                if arr[i][k+j] != arr[i][M+j-k-1]:
                    OX = False
                    break
            if OX:
                circular = arr[i][j:j+M]

    for j in range(N):
        for i in range(N-M+1):
            OX = True
            for k in range(M//2):
                if arr[k+i][j] != arr[M+i-k-1][j]:
                    OX = False
                    break
            if OX:
                for a in range(M):
                    circular += arr[i+a][j]

    print(f'#{tc} {circular}')