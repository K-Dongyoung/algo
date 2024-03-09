import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    count = {}

    for c in str1:
        count[c] = 0

    for c in str2:
        if count.get(c, -1) >= 0:
            count[c] += 1

    print(f"#{tc} {max(count.values())}")
