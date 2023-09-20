import sys
sys.stdin = open('cal.txt')
from collections import deque

def bfs(n, m):
    Q = deque()
    Q.append(n)
    visited[n] = 0
    while Q:
        v = Q.popleft()
        for n in [v+1, v-1, v*2, v-10]:
            if n == m:
                return visited[v] + 1
            if 0 < n <= 1000000 and not visited[n]:
                Q.append(n)
                visited[n] = visited[v] + 1
        # a = v+1
        # b = v-1
        # c = v*2
        # d = v-10
        # if a == m:
        #     return visited[v] + 1
        # if b == m:
        #     return visited[v] + 1
        # if c == m:
        #     return visited[v] + 1
        # if d == m:
        #     return visited[v] + 1
        # if 0<a<1000000 and not visited[a]:
        #     Q.append(a)
        #     visited[a] = visited[v] + 1
        # if 0<b<1000000 and not visited[b]:
        #     Q.append(b)
        #     visited[b] = visited[v] + 1
        # if 0<c<1000000 and not visited[c]:
        #     Q.append(c)
        #     visited[c] = visited[v] + 1
        # if 0<d<1000000 and not visited[d]:
        #     Q.append(d)
        #     visited[d] = visited[v] + 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    print(f'#{tc} {bfs(N, M)}')