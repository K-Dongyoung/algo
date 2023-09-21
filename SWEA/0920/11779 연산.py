import sys
sys.stdin = open('cal.txt')
from collections import deque
import math

def bfs(n, m):
    Q = deque()
    Q.append(n)
    cnt = 0

    while Q:
        v = Q.popleft()
        cnt += 1
        a = v+1
        b = v-1
        c = v*2
        d = v-10
        if a==m or b==m or c==m or d==m:
            return math.ceil(math.log(cnt, 4)) + 1

        Q.append(a)
        Q.append(b)
        Q.append(c)
        Q.append(d)




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N, M)}')

