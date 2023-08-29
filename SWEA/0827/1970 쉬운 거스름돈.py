import sys
sys.stdin = open('change.txt')
def change(n):
    result = [0] * 8
    L = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        result[i] += n//L[i]
        n %= L[i]
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    print(*change(N))