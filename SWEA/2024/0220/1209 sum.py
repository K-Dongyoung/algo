import sys
sys.stdin = open("input.txt")

for _ in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
        if sum_row > max_sum:
            max_sum = sum_row
        if sum_col > max_sum:
            max_sum = sum_col

    sum_left = 0
    sum_right = 0
    for i in range(100):
        sum_left += arr[i][i]
        sum_right += arr[i][100-i-1]
        if sum_left > max_sum:
            max_sum = sum_left
        if sum_right > max_sum:
            max_sum = sum_right

    print(f"#{tc} {max_sum}")