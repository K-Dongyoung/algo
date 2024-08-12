def solution(n, left, right):  # 시간 초과
    arr = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = i + 1 if i >= j else j + 1

    ans = []
    for i in range(n):
        ans += arr[i]
    return ans[left: right + 1]


def solution2(n, left, right):  # 런타임 에러
    arr = [0] * (n * n)
    for i in range(n):
        for j in range(n):
            if i * n + j <= right:
                arr[i * n + j] = i + 1 if i >= j else j + 1

    return arr[left:right + 1]


def solution3(n, left, right):  # 런타임 에러
    arr = [0] * (n * n)
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        arr[i] = a + 1 if a >= b else b + 1
    return arr[left:right + 1]


def solution4(n, left, right):  # 성공
    arr = [0] * (right - left + 1)
    for i in range(len(arr)):
        a = (i + left) // n
        b = (i + left) % n
        arr[i] = a + 1 if a >= b else b + 1
    return arr


print(solution4(3, 2, 5))
print(solution4(4, 7, 14))
print(solution4(10_000_000, 7, 14))
