import sys
sys.stdin = open('min_sum.txt')

def f(k, N, sum):
    global min_sum
    if k == N:
        print(temp, end=' ')
        sum_temp = 0
        for i in range(N):
            sum_temp += arr[i][temp[i]]
        print(sum_temp)
        # if min_sum > sum_temp:
        #     min_sum = sum_temp
        # print(sum)

    else:
        for i in range(k, N):
            temp[k], temp[i] = temp[i], temp[k]
            f(k+1, N, sum + arr[i][temp[i]])
            temp[k], temp[i] = temp[i], temp[k]



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp = [i for i in range(N)]
    min_sum = 0
    for i in range(N):
        min_sum += arr[i][0]
    f(0, N, 0)
    print(f'#{tc} {min_sum}')
    # ans = 0
    # print(f'#{tc} {ans}')