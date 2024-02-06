T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [[0] * W for _ in range(H)]

    num = 1
    for j in range(W):
        for i in range(H):
            arr[i][j] = num
            num += 1

    print(f'#{tc}')
    for i in range(H):
        print(*arr[i])