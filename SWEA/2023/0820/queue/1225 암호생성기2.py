import sys
sys.stdin = open('code.txt')

for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    a = min(arr)//15
    b = (a-1) * 15
    Q = [arr[i]-b for i in range(8)] + [0]*80

    front = -1
    rear = 7

    count = 0
    while True:
        front = front+1
        temp = Q[front] - (count%5+1)
        count += 1
        if temp <= 0:
            temp = 0
        rear = rear+1
        Q[rear] = temp
        if temp == 0:
            break

    print(f'#{tc}', *Q[front+1:rear+1])
