T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    row = 0
    for a in range(N):
        if arr[0][a] == 3:
            col = a
            break