import sys

sys.stdin = open("input.txt")


def f(N, d):
    count = 0
    while N % d == 0:
        N //= d
        count += 1
    return count


divisor = [2, 3, 5, 7, 11]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f"#{tc}", end=" ")
    for d in divisor:
        a = f(N, d)
        print(a, end=" ")
    print()
