import sys
sys.stdin = open('maze2.txt')

def decide_start(maze, N, x):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == x:
                return i, j


def path_finding(maze, N, sr, sc, x):
    visited = [[0]*N for _ in range(N)]
    Q = [0] * N * N
    front = -1
    rear = -1
    rear += 1
    Q[rear] = (sr, sc)
    visited[sr][sc] = 1
    while front != rear:
        front += 1
        vr, vc = Q[front]
        if maze[vr][vc] == x:
            return 1
        for m, n in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = vr + m
            nc = vc + n
            if 0<=nr<N and 0<=nc<N:
                if maze[nr][nc] != 1 and visited[nr][nc] == 0:
                    rear += 1
                    Q[rear] = (nr, nc)
                    visited[nr][nc] = visited[vr][vc] + 1
    return 0


for _ in range(10):
    tc = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]

    sr, sc = decide_start(maze, N, 2)
    print(f'#{tc} {path_finding(maze, N, sr, sc, 3)}')