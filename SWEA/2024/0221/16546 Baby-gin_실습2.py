import sys
sys.stdin = open("input.txt")

# 실패 런타임 에러

def find_triplet_triplet():
    counting_arr = [0] * 10
    for n in arr:
        counting_arr[n] += 1

    count = 0
    for i in range(10):
        if counting_arr[i] >= 3:
            count += 1
            counting_arr[i] -= 3
        if counting_arr[i] >= 3:
            count += 1
            counting_arr[i] -= 3

    if count == 2:
        return True
    else:
        return False

def find_run_run():
    counting_arr = [0] * 10
    for n in arr:
        counting_arr[n] += 1

    count = 0
    temp = []
    count_flag = 0
    for i in range(10):
        if counting_arr[i] > 0:
            temp.append(i)
            count_flag += 1
            if count_flag == 3:
                count += 1
                count_flag = 0
                for j in range(3):
                    counting_arr[   temp[j]] -= 1
        elif counting_arr[i] == 0:
            temp = []
            count_flag = 0

    temp = []
    for i in range(10):
        if counting_arr[i] == 1:
            temp.append(i)
            count_flag += 1
            if count_flag == 3:
                count += 1
                count_flag = 0
                for j in range(3):
                    counting_arr[temp[j]] -= 1
        elif counting_arr[i] == 0:
            temp = []
            count_flag = 0

    if count == 2:
        return True
    else:
        return False

def find_triplet_run():
    counting_arr = [0] * 10
    for n in arr:
        counting_arr[n] += 1

    count = 0
    for i in range(10):
        if counting_arr[i] >= 3:
            count += 1
            counting_arr[i] -= 3

    temp = []
    count_flag = 0
    for i in range(10):
        if counting_arr[i] > 0:
            temp.append(i)
            count_flag += 1
            if count_flag == 3:
                count += 1
                count_flag = 0
                for j in range(3):
                    counting_arr[temp[j]] -= 1
        elif counting_arr[i] == 0:
            temp = []
            count_flag = 0

    if count == 2:
        return True
    else:
        return False




T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))

    if find_run_run() or find_triplet_triplet() or find_triplet_run():
        ans = "true"
    else:
        ans = "false"

    print(f"#{tc} {ans}")