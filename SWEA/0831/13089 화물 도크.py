import sys
sys.stdin = open('dock.txt')

def f():
    f = 0
    for i in range(N):
        if f <= arr[i][0]:
            result.append(arr[i])
            f = arr[i][1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x:x[1])
    result = []
    f()
    print(f'#{tc} {len(result)}')

