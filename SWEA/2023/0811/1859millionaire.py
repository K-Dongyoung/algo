import sys
sys.stdin = open('millionaire.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_i = 0
    profit = 0

    while len(arr) > 1:
        for i in range(len(arr)):
            if arr[max_i] < arr[i]:
                max_i = i
        profit += arr[max_i]*max_i
        for i in range(max_i):
            profit -= arr[i]
        arr = arr[max_i+1:]
        max_i = 0


    print(f'#{tc} {profit}')