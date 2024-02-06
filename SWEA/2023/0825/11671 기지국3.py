import sys
sys.stdin = open('station.txt')

def c():
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                for k in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    for m in range(1, 4):
                        r = i + k[0] * m
                        c = j + k[1] * m
                        if 0<=r<n and 0<=c<n:
                            if arr[r][c] in station[m-1]:
                                arr[i][j] = 'X'
                                break
                    if arr[i][j] == 'X':
                        break

station = ['ABC', 'BC', 'C']

T = int(input())
for tc in range(1, T+1):
    n = int(input()) #2차원 배열 크기
    arr = [list(input()) for _ in range(n)] # H집, A 1기지국, B 2기지국, C 3기지국, X
    c()
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                count += 1
    print(f'#{tc} {count}')
