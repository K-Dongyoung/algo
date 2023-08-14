import sys
sys.stdin = open('fastest_string_typing.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)

    i = 0
    j = 0
    count = 0
    while i < a and j < b:
        if A[i] != B[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == b:
            count += 1
            j = 0

    print(f'#{tc} {a - (count*b) + count}')