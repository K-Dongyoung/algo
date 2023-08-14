import sys
sys.stdin = open('palindrome2.txt')

T = 10
for tc in range(1, T+1):
    temp = input()
    N = 100
    arr = [input() for _ in range(100)]
    max_l = 0

    for i in range(N):
        for k in range(1, N + 1):
            for j in range(N - k + 1):
                flag = True
                for m in range(k//2):
                    if arr[i][j+m] != arr[i][j+k-1-m]:
                        flag = False
                        break
                if flag:
                    if max_l < k:
                        max_l = k

    for i in range(N):
        for k in range(1, N + 1):
            for j in range(N - k + 1):
                flag = True
                for m in range(k//2):
                    if arr[j+m][i] != arr[j+k-1-m][i]:
                        flag = False
                        break
                if flag:
                    if max_l < k:
                        max_l = k



    print(f'#{tc} {max_l}')