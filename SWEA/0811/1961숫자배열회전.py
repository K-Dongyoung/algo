import sys
sys.stdin = open('num_arr_rotation.txt')

def rotate(arr):
    arr90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr90[j][N-1-i] = arr[i][j]
    return arr90

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr90 = rotate(arr)
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr90[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(arr180[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(arr270[i][j], end='')
        print()
