def solution(triangle):

    L = len(triangle)
    dp = [[] for _ in range(L)]
    dp[0].append(triangle[0][0])

    for i in range(1, L):
        for j in range(i + 1):
            left, right = 0, 0
            if j - 1 >= 0:
                left = dp[i - 1][j - 1]
            if j < i:
                right = dp[i - 1][j]
            dp[i].append(triangle[i][j] + max(left, right))

    answer = max(dp[L - 1])

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
