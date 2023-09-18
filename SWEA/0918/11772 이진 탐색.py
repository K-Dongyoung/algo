import sys
sys.stdin = open('binary.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    stack = []
    for b in B:
        s = 0
        e = len(A)-1
        while s <= e:
            m = (s + e) // 2

            if A[m] == b:
                cnt += 1
                break

            elif A[m] > b:
                e = m - 1
                if stack and stack[-1] == 'l':
                    break
                else:
                    stack.append('l')

            else:
                s = m + 1
                if stack and stack[-1] == 'r':
                    break
                else:
                    stack.append('r')

    print(cnt)