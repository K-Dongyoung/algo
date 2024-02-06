import sys
sys.stdin = open('GNS_test_input.txt')
sys.stdout = open('GNS_test_output.txt', 'w')

T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    arr = input().split()
    count_L = [0] * 10
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in range(N):
        for j in range(10):
            if arr[i] == number[j]:
                count_L[j] += 1

    print(tc)
    for i in range(10):
        print((number[i] + ' ') * count_L[i], end='')
    print()







