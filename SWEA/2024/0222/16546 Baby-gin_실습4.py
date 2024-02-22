import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().strip())) # strip을 붙이니 runtime error가 사라졌다. 뭔 차이일까?
    N = max(arr) + 1
    count = 0

    counting_arr = [0] * N
    for n in arr:
        counting_arr[n] += 1

    for i in range(N):
        if counting_arr[i] == 6:
            count += 2
            counting_arr[i] -= 6
            break
        if counting_arr[i] >= 3:
            count += 1
            counting_arr[i] -= 3

    for i in range(1, N - 1):
        if counting_arr[i - 1] > 0 and counting_arr[i] > 0 and counting_arr[i + 1] > 0:
            subtract = min(counting_arr[i - 1],  counting_arr[i], counting_arr[i + 1])
            count += subtract
            counting_arr[i - 1] -= subtract
            counting_arr[i] -= subtract
            counting_arr[i + 1] -= subtract

    print(f"#{tc} true") if count == 2 else print(f"#{tc} false")