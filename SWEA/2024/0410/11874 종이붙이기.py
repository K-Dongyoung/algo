import sys
sys.stdin = open("sample_input.txt")

m = [1, 1]
for i in range(2, 31):
    m.append(m[i - 1] + 2 * m[i - 2])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f"#{tc} {m[N // 10]}")

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input()) // 10
    a = 1
    b = 3
    for i in range(N - 2):
        c = b + 2 * a
        a = b
        b = c
    print(f"#{tc} {c}")
"""

"""
1 - 1
2 - 3
3 - 5
4 - 11
5 - 21
6 - 43
"""