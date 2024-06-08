from collections import deque

delta = ((1, 0), (0, 1), (0, -1), (-1, 0))


def bfs(v):
    q.append(v)

    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
                q.append((nr, nc))
                maze[nr][nc] = maze[r][c] + 1


N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

q = deque()

bfs((0, 0))

print(maze[N - 1][M - 1])
