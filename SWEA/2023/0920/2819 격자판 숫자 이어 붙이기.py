import sys
sys.stdin = open('grid.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]

