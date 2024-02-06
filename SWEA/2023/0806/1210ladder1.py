import sys
sys.stdin = open('ladder.txt')

def find_path(arr, c):
    visit = [[0] * 100 for _ in range(100)]
    r = 0
    while r < 98:
        for a in range(3):
            I = r + dr[a]
            J = c + dc[a]
            if 0 <= I < len(arr) and 0 <= J < len(arr):
                if arr[I][J] == 1 and visit[I][J] == 0:
                    r = I
                    c = J
                    visit[I][J] = 2345
                    break
    if arr[r + 1][c] == 2:
        return True
    else:
        return False


T = 10

dr = [0, 0, 1]
dc = [1, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[0][i] == 1:
            ans = find_path(arr, i)
            if ans:
                print(f'#{tc} {i}')
                break




