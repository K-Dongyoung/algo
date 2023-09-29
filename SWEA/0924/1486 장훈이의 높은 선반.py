import sys
sys.stdin = open('shelf.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    m = sum(H)

    for i in range(1<<N):
        s = 0

        for j in range(N):
            if i & (1<<j):
                s += H[j]

        if s >= B and m > s:
            m = s

    print(f'#{tc} {m - B}')