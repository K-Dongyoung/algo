import sys
sys.stdin = open('string_comparison.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()


    for i in range(len(str2) - len(str1) + 1):
        OX = 1
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                OX = 0
        if OX == 1:
            break

    print(f'#{tc} {OX}')
