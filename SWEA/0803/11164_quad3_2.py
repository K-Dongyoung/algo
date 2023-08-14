T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [[0] * W for _ in range(H)]
    num = 1

    for i in range(H):
        for j in range(W):
            arr[i][j + (W - 2*j - 1) * (i%2)] = num
            num += 1

    print(f'#{tc}')
    for i in range(H):
        print(*arr[i])