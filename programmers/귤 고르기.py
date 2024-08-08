def solution(k, tangerine):
    d = {}
    for t in tangerine:
        d[t] = d.setdefault(t, 0) + 1

    a = []
    for key, value in d.items():
        a.append([key, value])
    a.sort(reverse=True, key=lambda x: x[1])

    temp = 0
    answer = -1
    for i in range(len(a)):
        temp += a[i][1]
        if temp >= k:
            answer = i + 1
            break

    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
