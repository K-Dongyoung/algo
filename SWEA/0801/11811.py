T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input()))

    max_L = L[0]
    for num in L:
        if max_L < num:
            max_L = num

    C = [0] * (max_L + 1)

    for num in L:
        C[num] += 1

    max_i = 0
    for i in range(max_L + 1):
        if C[max_i] <= C[i]:
            max_i = i

    print(f'#{tc} {max_i} {C[max_i]}')