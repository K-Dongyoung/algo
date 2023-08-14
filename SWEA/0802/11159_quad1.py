T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = []
    print(f'#{tc}')
    for i in range(H):
        row = []
        for j in range(1, W+1):
            row.append(j + i*W)
            print(j + i*W, end=' ')
        print()
        arr.append(row)