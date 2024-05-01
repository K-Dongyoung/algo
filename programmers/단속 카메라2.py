def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # 나가는 지점 기준 오름차순 정렬
    L = len(routes)
    for i in range(L):
        if len(routes[i]) == 3:  # 카메라에 찍힌 차량이면 continue
            continue
        for j in range(i, L):  # i번째 차량 나가는 지점 기준으로 카메라 설치한다고 가정
            if len(routes[j]) == 3:  # 카메라에 찍힌 차량이면 continue
                continue
            if routes[i][1] < routes[j][0]:  # routes[i][1] 지점에 카메라가 설치될 것이므로 그보다 뒤에서 출발하는 차는 찍히지 않음
                continue
            routes[j].append(1)  # 감시 카메라 지나간 차량 방문 표시
        answer += 1
    return answer


A = [[0, 2], [2, 5], [4, 6], [6, 7], [5, 9], [8, 10]]
print(solution(A))