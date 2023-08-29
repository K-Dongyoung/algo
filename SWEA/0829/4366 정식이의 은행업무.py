import sys
sys.stdin = open('bank.txt')

T = int(input())
for tc in range(1, T+1):
    binary = input()
    tri = input()

    a = len(binary)
    b = len(tri)

    tmp1 = [0] * a
    for i in range(a):
        tmp1[i] = int(binary[i])

    tmp2 = [0] * b
    for i in range(b):
        tmp2[i] = int(tri[i])

    sum_list1 = set()
    for i in range(a):
        sum_tmp1 = 0
        tmp1[i] = (tmp1[i] + 1) % 2
        for j in range(a):
            sum_tmp1 += tmp1[j] * (2 ** (a-j-1))
        sum_list1.add(sum_tmp1)
        tmp1[i] = (tmp1[i] + 1) % 2

    sum_list2 = set()
    for i in range(b):
        sum_tmp2 = 0
        tmp2[i] = (tmp2[i] + 1) % 3
        for j in range(b):
            sum_tmp2 += tmp2[j] * (3 ** (b-j-1))
        sum_list2.add(sum_tmp2)

        sum_tmp2 = 0
        tmp2[i] = (tmp2[i] + 1) % 3
        for j in range(b):
            sum_tmp2 += tmp2[j] * (3 ** (b - j - 1))
        sum_list2.add(sum_tmp2)
        tmp2[i] = (tmp2[i] + 1) % 3


    print(f'#{tc}', (sum_list1&sum_list2).pop())


