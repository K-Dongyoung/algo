import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(len(progresses)):
        r = 100 - progresses[i]
        d = math.ceil(r / speeds[i])
        day.append(d)

    i = 0
    j = i + 1
    while i < len(day):
        cnt = 1
        while j < len(day) and day[i] >= day[j]:
            cnt += 1
            j += 1

        i = j
        j += 1
        answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
