"""
실패한 코드 입니다!
"""

def solution(routes):
    answer = 0
    routes.sort(reverse=True)
    L = len(routes)
    while routes:
        i = L - 1
        temp = [[0, []]]
        idx = 0
        for j in range(routes[i][0], routes[i][1] + 1):
            for k in range(L - 1, -1, -1):
                if routes[k][0] <= j <= routes[k][1]:
                    temp[idx][0] += 1
                    temp[idx][1].append(k)
            temp.append([0, []])
            idx += 1
        temp.sort(reverse=True)
        temp[0][1].sort(reverse=True)
        for index in temp[0][1]:
            routes.pop(index)
            L -= 1
        answer += 1
    return answer


A = [[-20, -19], [-18, -17], [-16, -15], [-14, -13], [-12, -11]]
print(solution(A))