import sys; sys.stdin = open('snail.txt')

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i = 0
    j = 0

    num = 1

    while True:

        arr[i][j] = num

        if num == N*N:
            break

        num += 1

        for k in range(4):
            I = i + di[k]
            J = j + dj[k]
            if 0 <= I < N and 0 <= J < N:
                if arr[I][J] == 0:
                    i = I
                    j = J
                    break

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])