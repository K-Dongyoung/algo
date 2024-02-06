T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):
        idx = i
        for j in range(i+1, N):
            if i % 2 == 0:
                if arr[idx] < arr[j]:
                    idx = j
            else:
                if arr[idx] > arr[j]:
                    idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()