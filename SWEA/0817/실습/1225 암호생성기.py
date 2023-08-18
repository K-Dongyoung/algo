import sys  #겨수님 코드 보기 간단함
sys.stdin = open('code.txt')

T = 10
for tc in range(1, T+1):
    N = input()
    arr = list(map(int, input().split()))
    Q = [0] * 1000 * 1000
    front = -1
    rear = -1

    for i in range(len(arr)):
        rear += 1
        Q[rear] = arr[i]

    temp = 0

    while Q[rear] > 0:
        for i in range(1, 6):
            front += 1
            if Q[front] - i <= 0:
                temp = 0
                rear += 1
                Q[rear] = temp
                break
            else:
                temp = Q[front] - i
                rear += 1
                Q[rear] = temp

    print(f'#{tc}', end=' ')
    for i in range(front+1, rear+1):
        print(Q[i], end=' ')
    print()