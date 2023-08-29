import sys
sys.stdin = open('harvesting.txt')

def f():
    sum = 0
    r = 0
    c = N//2
    sum += farm[r][c]
    farm[r][c] = -1
    i = 0

    while True:
        R = r + delta[i][0]
        C = c + delta[i][1]
        if 0<=R<N and 0<=C<N:
            if farm[R][C] != -1:
                sum += farm[R][C]
                farm[R][C] = -1
                r = R
                c = C
            else:
                R += 1
                sum += farm[R][C]
                farm[R][C] = -1
                r = R
                c = C
                i = (i + 1) % 4
        else:
            i = (i+1)%4
        if R > N//2:
            break
    return sum


delta = [(1,1),(1,-1),(-1,-1),(-1,1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {f()}')