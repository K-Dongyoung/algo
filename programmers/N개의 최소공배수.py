def solution(arr):
    d = {}
    for n in arr:
        a = n
        for m in range(2, n + 1):
            cnt = 0
            while a % m == 0:
                a //= m
                cnt += 1
            if cnt > 0 and d.setdefault(m, 0) < cnt:
                d[m] = cnt
            if a == 1:
                break
    ans = 1
    for k, v in d.items():
        ans *= (k ** v)
    return ans


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
