import sys
sys.stdin = open('fastest_string_typing.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)

    count = 0
    for i in range(a):
        flag = True
        for j in range(b):
            if i+j < a:
                if B[j] != A[i+j]:
                    flag = False
                    break
        if flag:
            count += 1



    print(f'#{tc} {a - (count * b) + count}')