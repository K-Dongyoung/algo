import sys
sys.stdin = open('container.txt')

def f():
    wl = len(W)
    tl = len(T)
    total = 0
    wi = 0
    ti = 0
    while True:
        if W[wi] <= T[ti]:
            total += W[wi]
            wi += 1
            ti += 1
        else:
            wi += 1
        if wi == wl or ti == tl:
            break
    return total


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort(reverse=True)
    T.sort(reverse=True)
    print(f'#{tc} {f()}')