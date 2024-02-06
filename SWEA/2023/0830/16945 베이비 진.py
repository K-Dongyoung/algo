import sys
sys.stdin = open('baby.txt')


def f(k, N):
    if k == N:
        for i in range(0, N, 3):
            if not (p[i] == p[i + 1] == p[i + 2]) and not (p[i] + 2 == p[i + 1] + 1 == p[i + 2]):
                return 0
        return 1
    else:
        for i in range(N):
            if used[i] == 0:
                p[k] = cards[i]
                used[i] = 1
                r = f(k + 1, N)
                if r == 1:
                    return 1
                used[i] = 0
    if k == 0:
        return 0


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input()))
    N = 6
    p = [0] * N
    used = [0] * N
    print(f'#{tc} {f(0, N)}')
