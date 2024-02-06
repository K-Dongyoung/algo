import sys; sys.stdin = open('gravity.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_h = 0
    for i in range(N-1):
        h = N - i - 1
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                h -= 1
        if max_h < h:
            max_h = h

    print(f'#{tc} {max_h}')
