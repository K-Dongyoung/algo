import sys
sys.stdin = open("input.txt")

def fun(arr, N, K):
    count = 0
    length = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                length += 1
            if arr[i][j] == 0:
                if length == K:
                    count += 1
                length = 0
        if length == K:
            count += 1
        length = 0
    return count


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle_t = list(map(list, zip(*puzzle)))
    print(f"#{tc} {fun(puzzle, N, K) + fun(puzzle_t, N, K)}")