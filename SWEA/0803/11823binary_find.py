T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    l = 1
    r = P
    count_a = 0
    count_b = 0

    while l < r:
        c = int((l+r) / 2)
        if A == c:
            count_a += 1
            break
        elif A > c:
            l = c
        else:
            r = c
        count_a += 1

    l = 1
    r = P
    while l < r:
        c = int((l+r) / 2)
        if B == c:
            count_b += 1
            break
        elif B > c:
            l = c
        else:
            r = c
        count_b += 1

    if count_a < count_b:
        print(f'#{tc} A')

    if count_a > count_b:
        print(f'#{tc} B')

    if count_a == count_b:
        print(f'#{tc} 0')