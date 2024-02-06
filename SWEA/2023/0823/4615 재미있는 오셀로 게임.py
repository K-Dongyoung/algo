import sys
sys.stdin = open('Othello.txt')

def create_arena(N):
    arena = [[0] * N for _ in range(N)]
    idx = (N-1)//2
    arena[idx][idx] = 2
    arena[idx][idx+1] = 1
    arena[idx+1][idx] = 1
    arena[idx+1][idx+1] = 2
    return arena

def find_opposite_color(r, c, color):
    result = []
    for i in range(8):
        R = r + dr[i]
        C = c + dc[i]
        if 0<=R<N and 0<=C<N:
            if arena[R][C] != 0:
                if arena[R][C] != color:
                    result.append(i)
    return result

def OX(r, c, color, L):
    result = []
    for i in L:
        for m in range(1, N):
            R = r + dr[i] * m
            C = c + dc[i] * m
            if 0 <= R < N and 0 <= C < N:
                if arena[R][C] == 0:
                    break
                elif arena[R][C] == color:
                    result.append(i)
                    break
    return result

def turn_over(r, c, color, L):
    arena[r][c] = color
    for i in L:
        for m in range(1, N):
            R = r + dr[i] * m
            C = c + dc[i] * m
            if 0 <= R < N and 0 <= C < N:
                if arena[R][C] == color:
                    break
                else:
                    arena[R][C] = color

def count(x, arr, N):
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == x:
                count += 1
    return count


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    arena = create_arena(N)

    for _ in range(M):
        r, c, color = map(int, input().split())
        direction = find_opposite_color(r-1, c-1, color)
        right_direction = OX(r-1, c-1, color, direction)
        turn_over(r-1, c-1, color, right_direction)

    black = count(1, arena, N)
    white = count(2, arena, N)

    print(f'#{tc} {black} {white}')

    for i in range(N):
        print(arena[i])