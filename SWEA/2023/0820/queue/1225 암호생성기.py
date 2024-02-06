import sys
sys.stdin = open('code.txt')

for _ in range(10):
    tc = int(input())
    Q = [0] + list(map(int, input().split()))

    front = 0
    rear = 8
    N = len(Q)

    count = 0
    while True:
        front = (front+1)%N
        temp = Q[front] - (count%5+1)
        count += 1
        if temp <= 0:
            temp = 0
        rear = (rear+1)%N
        Q[rear] = temp
        if temp == 0:
            break

    print(f'#{tc}', *Q[front+1:], *Q[:front])
