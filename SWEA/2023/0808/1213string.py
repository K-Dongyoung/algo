T = 10
for tc in range(1, T+1):
    temp = input()
    p = input()
    t = input()
    N = len(t)
    M = len(p)
    count = 0
    for i in range(N-M+1):
        flag = True
        for j in range(M):
            if p[j] != t[i+j]:
                flag = False
                break
        if flag:
            count += 1

    print(f'#{tc} {count}')