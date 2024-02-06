import sys
sys.stdin = open('rise.txt')

def mult():
    result = []
    for i in range(N):
        for j in range(i+1, N):
            temp = arr[i] * arr[j]
            result.append(temp)
    return result

def f():
    result = []
    for n in m:
        p = []
        tmp = n
        while tmp>0:
            p.append(tmp%10)
            tmp //= 10
        p.reverse()
        if sorted(p) == p:
            result.append(n)
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    m = mult()
    print(f'#{tc} {max(f())}')