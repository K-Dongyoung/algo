import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    length = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                length += 1
            if puzzle[i][j] == 0:
                if length == K:
                    count += 1
                length = 0
        if length == K:
            count += 1
        length = 0

    for i in range(N):
        for j in range(N):
            if puzzle[j][i] == 1:
                length += 1
            if puzzle[j][i] == 0:
                if length == K:
                    count += 1
                length = 0
        if length == K:
            count += 1
        length = 0

    print(f"#{tc} {count}")