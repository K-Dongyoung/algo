import sys
sys.stdin = open('sum_node.txt')

def postorder(n):
    if n <= N:
        a = postorder(n * 2)
        b = postorder(n * 2 + 1)
        return a + b + heap[n]
    return 0

T = int(input())
for tc in range(1, T+1):

    N, M, L = list(map(int, input().split()))
    heap = [0] * (N+1)

    for _ in range(M):
        leaf, num = map(int, input().split())
        heap[leaf] = num

    print(f'#{tc} {postorder(L)}')