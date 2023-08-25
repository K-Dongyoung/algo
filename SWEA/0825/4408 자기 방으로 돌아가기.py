import sys
sys.stdin = open('room.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    room = [0] * 201
    for _ in range(N):
        r1, r2 = map(int, input().split())
        r1 = (r1 + (r1 % 2)) // 2
        r2 = (r2 + (r2 % 2)) // 2
        for i in range(min(r1, r2), max(r1, r2) + 1):
            room[i] += 1

    print(f'#{tc} {max(room)}')