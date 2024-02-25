import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    red = set()
    blue = set()
    c = {1: red, 2: blue}
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                c[color].add((i, j))
    print(f"#{tc} {len(red & blue)}")
