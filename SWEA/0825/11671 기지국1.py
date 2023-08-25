import sys
sys.stdin = open('station.txt')

def c(n):
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                visited = False
                for k in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    for m in range(1, 4):
                        r = i + k[0] * m
                        c = j + k[1] * m
                        if 0<=r<n and 0<=c<n:
                            if arr[r][c] in station[m-1]:
                                visited = True
                                break
                        if visited:
                            break
                if not visited:
                    count += 1
    return count

station = ['ABC', 'BC', 'C']

T = int(input())
for tc in range(1, T+1):
    n = int(input()) #2차원 배열 크기
    arr = [input() for _ in range(n)] # H집, A 1기지국, B 2기지국, C 3기지국, X
    print(f'#{tc} {c(n)}')
