import sys
sys.stdin = open('prize.txt')

def pick2(L):
    temp = []
    for i in range(L-1):
        for j in range(i+1, L):
            temp.append((i, j))
    return temp

def nCr(n, r, s):
    global max_prize
    if r == 0:
        max_prize = max(max_prize, int(''.join(number)))
    else:
        for i in range(s, n):
            i1, i2 = two_idx[i]
            number[i1], number[i2] = number[i2], number[i1]
            nCr(n, r-1, i)
            number[i1], number[i2] = number[i2], number[i1]



T = int(input())
for tc in range(1, T+1):
    number, times = input().split()
    times = int(times)
    number = list(number)
    L = len(number)
    two_idx = pick2(L)
    T = len(two_idx)
    max_prize = 0
    nCr(T, times, 0)

    print(f'#{tc}', max_prize)
