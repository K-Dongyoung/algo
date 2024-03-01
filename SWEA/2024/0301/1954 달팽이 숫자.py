import sys
sys.stdin = open("snail.txt")

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    row = 0
    col = 0
    snail[0][0] = 1
    count = 2
    i = 0

    while count <= N * N:
        R, C = row + dr[i], col + dc[i]
        if 0 <= R < N and 0 <= C < N and snail[R][C] == 0:
            snail[R][C] = count
            count += 1
            row, col = R, C
        else:
            i = (i + 1) % 4

    print(f"#{tc}")
    for i in range(N):
        print(*snail[i])
