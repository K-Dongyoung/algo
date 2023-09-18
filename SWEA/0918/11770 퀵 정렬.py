import sys
sys.stdin = open('quick.txt')

def pivot(a, l, r):
    p = a[l]
    i = l
    j = r
    while i <= j:
        while i <= j and a[i] <= p: i += 1
        while i <= j and a[j] >= p: j -= 1
        if i < j: a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def quick_sort(a, l, r):
    if l < r:
        p = pivot(a, l, r)
        quick_sort(a, l, p-1)
        quick_sort(a, p+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')