import sys
sys.stdin = open("input.txt")

# 다른 사람 코드 참고함.
def f(arr, K):
    count = 0
    for _list in arr:
        arr2 = "".join(_list).split('0')
        for item in arr2:
            if item == '1' * K:
                count += 1
    return count

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [input().split() for _ in range(N)]
    puzzle_t = list(zip(*puzzle))
    print(f"#{tc} {f(puzzle, K) + f(puzzle_t, K)}")

