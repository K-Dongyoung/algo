T = 10
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    count = 0
    for i in range(2, N-2):
        side_max_height = 0
        for j in range(i-2, i+3):
            if j == i:
                continue
            if L[j] > side_max_height:
                side_max_height = L[j]
        if side_max_height < L[i]:
            count += L[i] - side_max_height

    print(f"#{tc} {count}")