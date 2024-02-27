import sys
sys.stdin = open("input.txt")

di = [0, 0, -1]
dj = [-1, 1, 0]

T = 10
for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2:
            x_end = i

    row = 99
    col = x_end

    while row > 0:
        for i in range(3):
            R = row + di[i]
            C = col + dj[i]
            if 0 <= R < 100 and 0 <= C < 100 and arr[R][C] == 1:
                row = R
                col = C
                arr[R][C] = 9

    print(f"#{tc} {col}")