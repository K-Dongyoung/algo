import sys
sys.stdin = open("input.txt")

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                row_i = i + di[k]
                col_i = j + dj[k]
                if 0 <= row_i < N and 0 <= col_i < N:
                    difference = arr[i][j] - arr[row_i][col_i]
                    if difference >= 0:
                        answer += difference
                    else:
                        answer -= difference

    print(f"#{tc} {answer}")