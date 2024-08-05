def solution(n):
    a = [0] * (n + 1)
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n] % 1234567


print(solution(100000))
print(solution(5))
