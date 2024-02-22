import sys
sys.stdin = open("input.txt")

#실패 런타임 에러

N = 10
T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))

    count = 0

    counting_arr = [0] * N
    for n in arr:
        counting_arr[n] += 1

    if max(counting_arr) >= 3:
        for i in range(N):
            if counting_arr[i] == 6:
                count += 2
                counting_arr[i] -= 6
            if counting_arr[i] >= 3:
                count += 1
                counting_arr[i] -= 3

    temp = []
    count_flag = 0
    for i in range(N):
        if counting_arr[i] > 0:
            temp.append(i)
            count_flag += 1
            if count_flag == 3:
                count += 1
                count_flag = 0
                for j in range(3):
                    counting_arr[temp[j]] -= 1
                temp = []
        elif counting_arr[i] == 0:
            temp = []
            count_flag = 0

    if max(counting_arr) == 1:
        temp = []
        count_flag = 0
        for i in range(N):
            if counting_arr[i] == 1:
                temp.append(i)
                count_flag += 1
                if count_flag == 3:
                    count += 1
                    count_flag = 0
                    for j in range(3):
                        counting_arr[temp[j]] -= 1
                    temp = []
            elif counting_arr[i] == 0:
                temp = []
                count_flag = 0

    if count == 2:
        ans = "true"
    else:
        ans = "false"

    print(f"#{tc} {ans}")