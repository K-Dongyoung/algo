import sys
sys.stdin = open('station.txt')

def count_H(n):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            for m in range(1, 4):
                if arr[i][j] == station[m-1]:
                    for a in range(1, m+1):
                        for k in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            r = i + k[0] * a
                            c = j + k[1] * a
                            if 0<=r<n and 0<=c<n:
                                if arr[r][c] == 'H' and visited[r][c] == 0:
                                    count += 1
                                    visited[r][c] = 1
    return count

station = ['A', 'B', 'C']

T = int(input())
for tc in range(1, T+1):
    n = int(input()) #2차원 배열 크기
    arr = [input() for _ in range(n)] # H집, A 1기지국, B 2기지국, C 3기지국, X
    Home = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                Home += 1
    print(f'#{tc} {Home - count_H(n)}')