import sys
sys.stdin = open('binary_search.txt')

def inorder(n):
    global num
    if n <= N:
        inorder(n * 2)
        heap[n] = num
        num += 1
        inorder(n * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)

    num = 1
    inorder(1)
    print(f'#{tc} {heap[1]} {heap[N//2]}')