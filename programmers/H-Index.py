def solution(citations):
    answer = 0
    for h in range(1, 10001):
        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                cnt += 1
            if cnt >= h:
                answer = h
                break
        if answer < h:
            break

    return answer


print(solution([3, 0, 6, 1, 5]))
