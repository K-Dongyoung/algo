def solution(triangle):
    answer = 0
    a = len(triangle) - 1
    for i in range(1 << a):
        r, c = 0, 0
        sum = triangle[r][c]
        for j in range(a):
            if i & (1 << j):
                r += 1
                c += 1
                sum += triangle[r][c]
            else:
                r += 1
                sum += triangle[r][c]
        if sum > answer:
            answer = sum

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
