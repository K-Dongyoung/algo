import sys
sys.stdin =open('view.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    view_count = 0
    for i in range(2, N-2):
        max_temp = 0
        for j in range(-2, 3):
            if j:
                if max_temp < arr[i+j]:
                    max_temp = arr[i+j]
        if arr[i] >= max_temp:
            view_count += arr[i] - max_temp

    print(f'#{tc} {view_count}')
