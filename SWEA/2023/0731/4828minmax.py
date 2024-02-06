T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_max = arr[0]
    arr_min = arr[0]
    for num in arr:
        if num > arr_max:
            arr_max = num
        if num < arr_min:
            arr_min = num
    difference = arr_max - arr_min
    print(f'#{i+1} {difference}')

