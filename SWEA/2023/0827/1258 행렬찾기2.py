import sys
sys.stdin = open('arr.txt')

def find_arr():
    result = []
    matrix = [0] * (n+1)
    for j in range(n):
        cnt = 0
        for i in range(n):
            if house[i][j] > 0:
                cnt += 1
            else:
                if cnt > 0:
                    matrix[cnt] += 1
                    cnt = 0
    for i in range(len(matrix)):
        if matrix[i] > 0:
            result.append([i*matrix[i], i, matrix[i]])
    result.sort()
    return result


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    house = [list(map(int, input().split())) for _ in range(n)]
    result = find_arr()
    print(f'#{tc} {len(result)}', end=' ')
    for i in range(len(result)):
        print(*result[i][1:], end=' ')
    print()