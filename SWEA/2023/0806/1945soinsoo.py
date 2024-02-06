import sys

sys.stdin = open('soinsoo.txt')


def func_ans(N, x):
    count = 0
    while N % x == 0:
        count += 1
        N //= x

    return count


T = int(input())
arr = [2, 3, 5, 7, 11]
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}', end=' ')
    for num in arr:
        print(func_ans(N, num), end=' ')
    print()