import sys
sys.stdin = open('Othello.txt')

def create_arena(N):
    arena = [[0] * N for _ in range(N)]
    for i in range(N//2, N//2+2):
        arena[i][i] = 2
        arena[i][i+1] = 1
        arena[i+1][i] = 1
        arena[i+1][i+1] = 2
    return arena

def find_opposite_color():
    pass

def turn_over():
    pass



dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

