import sys
sys.stdin = open('binary.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    r = 0
    l = 0
    for b in B:
        s = 0
        e = len(A)-1
        while s <= e:
            m = (s + e) // 2
            if m == b :
