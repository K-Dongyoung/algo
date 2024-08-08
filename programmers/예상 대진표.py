def solution(n,a,b):
    cnt = 1
    while (a + 1) // 2  != (b + 1) // 2:
        a = (a + 1) // 2
        b = (b + 1) // 2
        cnt += 1
    return cnt


print(solution(8, 4, 7))
