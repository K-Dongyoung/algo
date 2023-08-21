import sys
sys.stdin = open('중위순회.txt')

def inorder(n):
    if n <= N:
        inorder(n*2)
        print(arr[n], end='')
        inorder(n*2+1)


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)


    for i in range(1, N+1):
        arr[i] = input().split()[1]


    print(f'#{tc}', end=' ')
    inorder(1)
    print()
