import sys
sys.stdin = open('binary_heap.txt')

def enQ():
    for i in range(N):
        c = i + 1
        p = c//2
        while p and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c//2

def ancestor(n):
    result = []
    c = n
    p = c // 2
    while p:
        result.append(heap[p])
        c = p
        p =c//2
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0] + list(map(int, input().split()))

    enQ()
    ancestor_L = ancestor(N)
    print(f'#{tc} {sum(ancestor_L)}')