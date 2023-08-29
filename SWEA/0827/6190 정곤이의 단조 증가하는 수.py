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
    max = -1
    for n in m:
        tmp = n
        a = tmp%10
        tmp //= 10
        while tmp>0:
            b = tmp%10
            if a < b:
                break
            a = b
            tmp //= 10
        if tmp == 0 and max < n:
            max = n
    return max

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    m = mult()
    print(f'#{tc} {f()}')