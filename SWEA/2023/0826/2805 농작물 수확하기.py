import sys
sys.stdin = open('harvesting.txt')
# def f():
    # i = 0
    # k = 0
    # while i < N:
    #     for j in range(N // 2 - delta[k], N // 2 + delta[k] + 1):
    #         sum += farm[i][j]
    #     i += 1
    #     k += 1
    # return sum

def f():
    sum = 0
    for i in range(N):
        for j in range(N // 2 - delta[i], N // 2 + delta[i] + 1):
            sum += farm[i][j]
    return sum


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    delta = [i for i in range(N // 2 + 1)] + [i for i in range(N // 2 - 1, -1, -1)]
    print(f'#{tc} {f()}')