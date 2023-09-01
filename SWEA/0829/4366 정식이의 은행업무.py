import sys
sys.stdin = open('bank.txt')

T = int(input())
for tc in range(1, T+1):
    binary = list(map(int, input()))
    tri = list(map(int, input()))

    a = len(binary)
    b = len(tri)

    sum_list1 = set()
    for i in range(a):
        sum_tmp1 = 0
        binary[i] = (binary[i] + 1) % 2
        for j in range(a):
            sum_tmp1 += binary[j] * (2 ** (a - j - 1))
        sum_list1.add(sum_tmp1)
        binary[i] = (binary[i] + 1) % 2

    sum_list2 = set()
    for i in range(b):
        sum_tmp2 = 0
        tri[i] = (tri[i] + 1) % 3
        for j in range(b):
            sum_tmp2 += tri[j] * (3 ** (b - j - 1))
        sum_list2.add(sum_tmp2)

        sum_tmp2 = 0
        tri[i] = (tri[i] + 1) % 3
        for j in range(b):
            sum_tmp2 += tri[j] * (3 ** (b - j - 1))
        sum_list2.add(sum_tmp2)
        tri[i] = (tri[i] + 1) % 3

    print(f'#{tc}', (sum_list1&sum_list2).pop())