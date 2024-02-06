import sys
sys.stdin = open('rotate.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = [0] + list(map(int, input().split()))
    front = 0
    rear = N

    for _ in range(M):
        front = (front+1)%(N+1)
        temp = Q[front]
        rear = (rear+1)%(N+1)
        Q[rear] = temp

    print(f'#{tc} {Q[(front+1)%(N+1)]}')