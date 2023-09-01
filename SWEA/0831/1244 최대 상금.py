import sys
sys.stdin = open('prize.txt')

def f():
    cnt = 0
    for i in range(len(number)-1):
        maxi = i
        for j in range(i+1, len(number)):
            if number[maxi] <= number[j]:
                maxi = j
        if maxi != i:
            number[i], number[maxi] = number[maxi], number[i]
            cnt += 1
        if cnt == change:
            return

    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            if number[i] == number[j]:
                return
    for i in range(change-cnt):
        number[-1], number[-2] = number[-2], number[-1]


T = int(input())
for tc in range(1, T+1):
    number, change = input().split()
    change = int(change)
    number = list(number)
    f()
    print(f'#{tc}', ''.join(number))
