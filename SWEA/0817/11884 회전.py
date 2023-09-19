import sys
sys.stdin = open('rotate.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    Q = [0] * (N+M+1)
    front = -1
    rear = -1

    for i in range(N):
        rear += 1
        Q[rear] = arr[i]

    temp = 0

    for i in range(M):
        front += 1
        temp = Q[front]
        rear += 1
        Q[rear] = temp

    print(f'#{tc} {Q[front+1]}')
