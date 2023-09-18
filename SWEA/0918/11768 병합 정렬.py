import sys
sys.stdin = open('merge.txt')
from collections import deque

def merge(l, r):
    global cnt
    result = deque()
    if l[-1] > r[-1]:
        cnt += 1
    while l and r:
        if l[0] >= r[0]:
            result.append(r.popleft())
        else:
            result.append(l.popleft())
    if l:
        result.extend(l)
    if r:
        result.extend(r)
    return result


def merge_sort(a, n):
    if n == 1:
        return a
    else:
        left = a[0:n//2]
        right = a[n//2:n]

        left = merge_sort(left, n//2)
        right = merge_sort(right, n//2 + n%2)

        return merge(deque(left), deque(right))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    A = merge_sort(arr, N)
    print(f'#{tc} {A[N//2]} {cnt}')