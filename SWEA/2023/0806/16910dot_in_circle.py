import sys
sys.stdin = open('dot_in_circle.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 4*N + 1
    count_temp = 0
    for x in range(1, N+1):
        for y in range(1, N+1):
            if x*x + y*y <= N*N:
                count_temp += 1

    count_temp *= 4
    count += count_temp

    print(f'#{tc} {count}')