import sys

sys.stdin = open("input.txt")


def f(matrix, n, m):
    for string in matrix:
        for i in range(n - m + 1):
            for j in range(m // 2):
                if string[i + j] != string[i + m - j - 1]:
                    break
                if j == m // 2 - 1:
                    return string[i: i + m]
    return False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr_t = list(zip(*arr))
    if f(arr, N, M):
        ans = f(arr, N, M)
    else:
        ans = "".join(f(arr_t, N, M))
    print(f"#{tc} {ans}")
