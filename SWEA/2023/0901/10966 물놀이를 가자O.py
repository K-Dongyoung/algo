import sys
sys.stdin = open('water.txt')

from collections import deque

def find_water(arr):
    global queue
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 1

def bfs():
    global ans
    global queue
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            R = r + di[i]
            C = c + dj[i]
            if 0<=R<N and 0<=C<M and landscape[R][C] == 'L':
                if visited[R][C] == 0:
                    queue.append((R, C))
                    visited[R][C] = visited[r][c] + 1
                    ans += visited[r][c]
                elif visited[R][C] > visited[r][c] + 1:
                    queue.append((R, C))
                    ans += visited[r][c]
                    ans -= visited[R][C]
                    visited[R][C] = visited[r][c] + 1


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    landscape = []
    for i in range(N):
        tmp = input()
        landscape.append(tmp)
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    ans = 0

    find_water(landscape)
    bfs()

    print(f'#{tc} {ans}')