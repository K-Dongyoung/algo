import sys
sys.stdin = open('rise.txt')

def f():
    for i in range(N):
        for j in range(i+1, N):
            X = arr[i] * arr[j]
            flag = True
            tmp = X
            a = tmp % 10
            tmp //= 10
            while tmp > 0:
                b = tmp % 10
                if a < b:
                    flag = False
                    break
                a = b
                tmp //= 10
            if flag:
                return X
    return -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()

    print(f'#{tc} {f()}')