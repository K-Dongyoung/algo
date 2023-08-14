import sys
sys.stdin = open('noob_palindrome.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    OX = 1
    for i in range(len(str1)//2):
        if str1[i] != str1[len(str1)-1-i]:
            OX = 0
            break

    print(f'#{tc} {OX}')