import sys
sys.stdin = open('card.txt')


def g(i, j):
    if arr[i] == arr[j] + 1:
        return i
    elif arr[j] == arr[i] + 1:
        return j
    elif arr[i] == arr[j] + 2:
        return j
    elif arr[j] == arr[i] + 2:
        return i
    else:
        return i


def f(s, e):
    if s == e:
        return s
    else:
        r1 = f(s, (s + e) // 2)
        r2 = f((s + e) // 2 + 1, e)
        return g(r1, r2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {f(0, N-1)+1}')
