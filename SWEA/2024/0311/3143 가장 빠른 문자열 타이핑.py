import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    # answer = len(A.replace(B, "b"))
    # print(f"#{tc} {answer}")
    lenA = len(A)
    lenB = len(B)
    count = 0

    # for i in range(lenA - lenB + 1):
    #     for j in range(lenB):
    #         if A[i + j] != B[j]:
    #             break
    #         if j == lenB - 1:
    #             count += 1

    # 위 코드 안되는 이유 : aaaaa aa 같은 경우 답을 4로 출력한다.
    # for이 아닌 while로 해야함!

    i = j = 0
    while i < lenA:
        while i < lenA and j < lenB:
            if A[i] != B[j]:
                i -= j
                j = -1
            i += 1
            j += 1
        if j == lenB:
            count += 1
            j = 0

    print(f"#{tc} {lenA - count * lenB + count}")