T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1 << len(A)):
        sum_subset = 0
        num_subset = 0
        for j in range(len(A)):
            if i & (1 << j):
                sum_subset += A[j]
                num_subset += 1
        if num_subset == N and sum_subset == K:
            ans += 1

    print(f'#{tc} {ans}')
