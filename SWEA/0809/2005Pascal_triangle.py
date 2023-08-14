import sys
sys.stdin = open('tri.txt')

def pascal_tri(N):
    arr = [0] * (N+1)
    if N == 1 and N == 2:
        return [0] + [1]*N
    for i in range(1, N+1):
        if i == 1 or i == N:
            arr[i] = 1
        else:
            arr[i] = pascal_tri(N-1)[i-1] + pascal_tri(N-1)[i]
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    for i in range(1, N+1):
        L = pascal_tri(i)
        for j in range(1, len(L)):
            print(L[j], end=' ')
        print()
