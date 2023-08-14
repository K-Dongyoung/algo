import sys
sys.stdin = open('글자수.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    max_count = 0
    for i in range(N):
        count = 0
        for j in range(M):
            if str1[i] == str2[j]:
                count += 1
        if max_count < count:
            max_count = count

    print(f'#{tc} {max_count}')