import sys
sys.stdin = open("input.txt")

def f(s):
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[l - i - 1]:
            break
        if i == l // 2 - 1:
            return 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    word = input()
    print(f"#{tc} {f(word)}")