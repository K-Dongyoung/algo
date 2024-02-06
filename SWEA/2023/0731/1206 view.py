for tc in range(1, 11):
    N = int(input())
    temp = list(map(int, input().split()))
    L_height = [0] * 2 + temp + [0] * 2
    count = 0
    for i in range(2, len(L_height) - 2):
        for j in range(L_height[i], 0, -1):
            if j > L_height[i+1] and j > L_height[i+2] and j > L_height[i-1] and j > L_height[i-2]:
                count += 1
    print(f'#{tc} {count}')