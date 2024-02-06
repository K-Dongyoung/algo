import sys
sys.stdin = open('hunter.txt')

def find_hunter(arr):
    hunter = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                hunter.append((i, j))
    return hunter

def rabbit(L, arr):
    count = 0
    for i, j in L:
        for k in range(8):
            for m in range(1, N+1):
                R = i + dr[k] * m
                C = j + dc[k] * m
                if 0<=R<N and 0<=C<N:
                    if arr[R][C] == 2:
                        count += 1
                    if arr[R][C] == 3:
                        break
    return count


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {rabbit(find_hunter(arr), arr)}')