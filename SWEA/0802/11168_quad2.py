T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    print(f'#{tc}')
    for i in range(H):
        for j in range(W):
            print(H*j + i + 1, end=' ')
        print()