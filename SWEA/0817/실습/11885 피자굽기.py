import sys
sys.stdin = open('pizza.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))


    Q = [0] * 10000
    front = -1
    rear = -1


    count = [0] * len(Ci)
    for i in range(M):
        temp = Ci[i]
        while temp > 0:
            temp //= 2
            count[i] += 1



    print(count)