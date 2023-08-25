import sys
sys.stdin = open('mirror.txt')

def light(r, c, di, N):
    count = 0
    R = r + d[di][0]
    C = c + d[di][1]
    while 0<=R<N and 0<=C<N:
        if arr[R][C] == 1:
            count += 1
            di = m1[di]
        elif arr[R][C] == 2:
            count += 1
            di = m2[di]
        R = R + d[di][0]
        C = C + d[di][1]
    return count


d = [(0,1), (1,0), (0,-1), (-1,0)]
m1 = [3, 2, 1, 0]
m2 = [1, 0, 3, 2]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {light(0, 0, 0, N)}')