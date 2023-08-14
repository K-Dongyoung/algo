import sys; sys.stdin = open('vocawhere.txt')

def find_ans(arr, N, K):
    count = 0
    for i in range(N):
        len = 0
        for j in range(N):
            if arr[i][j] == 1:
                len += 1
            if arr[i][j] == 0 or j == N - 1:
                if K == len:
                    count += 1
                len = 0
    return count

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    w_count = find_ans(arr, N, K)
    h_count = find_ans(list(zip(*arr)), N, K)
    count = w_count + h_count

    print(f'#{tc} {count}')

    # count = 0
    # for i in range(N):
    #     len_w = 0
    #     len_h = 0
    #     for j in range(N):
    #         if arr[i][j] == 1:
    #             len_w += 1
    #         if arr[i][j] == 0 or j == N - 1:
    #             if K == len_w:
    #                 count += 1
    #             len_w = 0
    #
    #         if arr[j][i] == 1:
    #             len_h += 1
    #         if arr[j][i] == 0 or i == N - 1:
    #             if K == len_h:
    #                 count += 1
    #             len_h = 0

    print(f'#{tc} {count}')