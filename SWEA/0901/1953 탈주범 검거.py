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
        if sewer[r][c] == 1:
            for i in range(4):
                R = r + di[i]
                C = c + dj[i]
                if 0<=R<N and 0<=C<M and visited[R][C] == 0 and sewer[R][C] > 0:
                    queue.append((R, C))
                    visited[R][C] = 1

        elif sewer[r][c] == 2:
            for i in [0, 2]:
                R = r + di[i]
                C = c + dj[i]
                if 0 <= R < N and 0 <= C < M and visited[R][C] == 0 and sewer[R][C] > 0:
                    queue.append((R, C))
                    visited[R][C] = 1

        elif sewer[r][c] == 3:
            for i in [1, 3]:
                R = r + di[i]
                C = c + dj[i]
                if 0 <= R < N and 0 <= C < M and visited[R][C] == 0 and sewer[R][C] > 0:
                    queue.append((R, C))
                    visited[R][C] = 1

        elif sewer[r][c] == 4:
            for i in [0, 1]:
                R = r + di[i]
                C = c + dj[i]
                if 0 <= R < N and 0 <= C < M and visited[R][C] == 0 and sewer[R][C] > 0:
                    queue.append((R, C))
                    visited[R][C] = 1

        elif sewer[r][c] == 5:
            for i in [2, 1]:
                R = r + di[i]
                C = c + dj[i]
                if 0 <= R < N and 0 <= C < M and visited[R][C] == 0 and sewer[R][C] > 0:
                    queue.append((R, C))
                    visited[R][C] = 1

        elif sewer[r][c] == 6:
            for i in [2, 3]:
                R = r + di[i]
                C = c + dj[i]
                if 0 <= R < N and 0 <= C < M and visited[R][C] == 0 and sewer[R][C] > 0:
                    queue.append((R, C))
                    visited[R][C] = 1

        elif sewer[r][c] == 7:
            for i in [0, 3]:
                R = r + di[i]
                C = c + dj[i]
                if 0 <= R < N and 0 <= C < M and visited[R][C] == 0 and sewer[R][C] > 0:
                    queue.append((R, C))
                    visited[R][C] = 1

        time += 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    sewer = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    time = 1
    count = 1

    bfs(R, C)
    # ans = 0
    # for i in range(N):
    #     ans += sum(visited[i])
    #
    # print(f'#{tc} {ans}')

    for i in range(N):
        print(visited[i])