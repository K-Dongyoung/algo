import sys
sys.stdin = open('grid.txt')


def perm(n, k, str):
    if k == n:
        pass
    else:
        for i in range(4):
            if 0<=di[i]<4 and 0<=dj[i]<4:
                perm(n, k+1, str + arr[di][dj])


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    d = [0, 1, 2, 3]
    for i in range(4):
        for j in range(4):
            perm(6, 0, arr[i][j])