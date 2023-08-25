import sys
sys.stdin = open('오목.txt')

def f():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(8):
                    count = 1
                    for m in range(1, 5):
                        r = i + di[k] * m
                        c = j + dj[k] * m
                        if 0<=r<N and 0<=c<N:
                            if arr[r][c] == 'o':
                                count += 1
                    if count == 5:
                        return 'YES'
    return 'NO'



di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print(f'#{tc} {f()}')