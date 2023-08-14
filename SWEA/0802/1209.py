T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    total_max = 0
    for i in range(100):
        sum_temp = 0
        sum_temp2 = 0
        for j in range(100):
            sum_temp += arr[i][j]
            sum_temp2 += arr[j][i]
        if total_max < sum_temp:
            total_max = sum_temp
        if total_max < sum_temp2:
            total_max = sum_temp2

    sum_temp = 0
    sum_temp2 = 0
    for i in range(100):
        sum_temp += arr[i][i]
        sum_temp2 += arr[99 - i][i]
    if total_max < sum_temp:
        total_max = sum_temp
    if total_max < sum_temp2:
        total_max = sum_temp2

    print(f'#{tc} {total_max}')