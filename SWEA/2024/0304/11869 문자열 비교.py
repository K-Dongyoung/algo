import sys
sys.stdin = open("sample_input.txt")

def f(s1, s2):
    M = len(s2)
    N = len(s1)
    for i in range(M - N + 1):
        for j in range(N):
            if s1[j] != s2[i + j]:
                break
            if j == N - 1:
                return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    print(f"#{tc} {f(str1, str2)}")