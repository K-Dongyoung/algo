import sys
sys.stdin = open("test_input.txt")

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    str1 = input()
    str2 = input()
    count = 0

    l1 = len(str1)
    l2 = len(str2)

    for i in range(l2 - l1 + 1):
        for j in range(l1):
            if str2[i + j] != str1[j]:
                break
            if j == l1 - 1:
                count += 1

    print(f"#{tc} {count}")