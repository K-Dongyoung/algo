import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1

    print(f"#{tc}")

    for i in range(N):
        for j in range(i + 1):
            row = i - 1
            left_col = j - 1
            if row >= 0:
                arr[i][j] += arr[row][j]
                if left_col >= 0:
                    arr[i][j] += arr[row][left_col]
            if arr[i][j] > 0:
                print(arr[i][j], end=" ")
        print()