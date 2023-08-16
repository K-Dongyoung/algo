import sys
sys.stdin = open('card.txt')


def f(s, e):
    if s == e:
        print(arr[s], end=' ')
    else:
        f(s, (s + e) // 2)
        f((s + e) // 2 + 1, e)



T = int(input())
for tc in range(1):
    N = int(input())
    arr = list(map(int, input().split()))
    f(0, N-1)
    print()