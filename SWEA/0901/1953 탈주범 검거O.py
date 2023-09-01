import sys
sys.stdin = open('criminal.txt')
from collections import deque

def bfs(r, c):
    global time
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        if time == L:
            return
        r, c = queue.popleft()
        for i in d[sewer[r][c]]:
            R = r + i[0]
            C = c + i[1]
            if 0<=R<N and 0<=C<M:
                if i == (-1, 0) and sewer[R][C] in up:
                elif i == (1, 0) and sewer[R][C] in down:
                elif i == (0, -1) and sewer[R][C] in left:
                elif i == (0, 1) and sewer[R][C] in right:
        time += 1

d ={
    1:[(-1, 0), (1, 0), (0, -1), (0, 1)],
    2:[(-1, 0), (1, 0)],
    3:[(0, -1), (0, 1)],
    4:[(-1, 0), (0, 1)],
    5:[(1, 0), (0, 1)],
    6:[(1, 0), (0, -1)],
    7:[(-1, 0), (0, -1)]
}
up = [1, 2, 5, 6]
down = [1, 2, 4, 7]
left = [1, 3, 4, 5]
right = [1, 3, 6, 7]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    sewer = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    time = 1
    bfs(R, C)