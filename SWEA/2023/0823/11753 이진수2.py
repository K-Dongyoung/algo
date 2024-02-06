import sys
sys.stdin = open('binary2.txt')

def f(N):
    result = ''
    count = 0
    while N:
        N = N * 2
        result += str(int(N))
        N -= int(N)
        count += 1
        if count >= 13:
            return 'overflow'
    return result


T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {f(N)}')
