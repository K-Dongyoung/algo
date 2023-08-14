import sys
sys.stdin = open('flatten.txt')

T =10
for tc in range(1, T+1):
    dump = int(input())
    L = list(map(int, input().split()))

    for _ in range(dump):
        max_i = 0
        min_i = 0
        for i in range(len(L)):
            if L[max_i] < L[i]:
                max_i = i
            if L[min_i] > L[i]:
                min_i = i
        L[max_i] -= 1
        L[min_i] += 1

    max_i = 0
    min_i = 0
    for i in range(len(L)):
        if L[max_i] < L[i]:
            max_i = i
        if L[min_i] > L[i]:
            min_i = i

    print(f'#{tc} {L[max_i] - L[min_i]}')
