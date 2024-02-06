import sys
sys.stdin = open('pizza.txt')
from collections import deque

def f():
    Q = deque()
    for i in range(N):
        Q.append(i)
    idx = N

    while len(Q) > 1:
        pizza = Q.popleft()
        Ci[pizza] //= 2
        if Ci[pizza] != 0:
            Q.append(pizza)
        elif idx < M:
            Q.append(idx)
            idx += 1

    return Q.popleft() + 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    print(f'#{tc} {f()}')