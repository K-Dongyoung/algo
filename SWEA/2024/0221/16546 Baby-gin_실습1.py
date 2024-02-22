import sys
sys.stdin = open("input.txt")

# 실패 런타임 에러
def find_baby_gin(arr):
    count = 0
    counting_arr = [0] * 10
    for n in arr:
        counting_arr[n] += 1
        if counting_arr[n] == 3:
            count += 1
            counting_arr[n] = 0
        elif n - 2 >= 0 and counting_arr[n - 2] == 1 and counting_arr[n - 1] == 1:
            count += 1
            counting_arr[n - 2] = 0
            counting_arr[n - 1] = 0
            counting_arr[n] = 0
        elif n + 2 <= 9 and counting_arr[n + 2] == 1 and counting_arr[n + 1] == 1:
            count += 1
            counting_arr[n + 2] = 0
            counting_arr[n + 1] = 0
            counting_arr[n] = 0
        elif 1 <= n <= 8 and counting_arr[n - 1] == 1 and counting_arr[n + 1] == 1:
            count += 1
            counting_arr[n - 1] = 0
            counting_arr[n + 1] = 0
            counting_arr[n] = 0
    if count == 2:
        return 'true'
    else:
        return 'false'


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))

    print(f"#{tc} {find_baby_gin(arr)}")

