def solution(arr1, arr2):
    row1 = len(arr1)
    col2 = len(arr2[0])
    answer = [[0] * col2 for _ in range(row1)]
    arr2_t = list(zip(*arr2))
    for i in range(row1):
        for j in range(col2):
            answer[i][j] = mlist(arr1[i], arr2_t[j])
    return answer


def mlist(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total


def solution2(arr1, arr2):  # 다른 사람 풀이 참조
    ans = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr1[0])):
                total += arr1[i][k] * arr2[k][j]
            row.append(total)
        ans.append(row)
    return ans


print(solution2([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution2([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
