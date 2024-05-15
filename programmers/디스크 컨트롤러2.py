import heapq

def solution(jobs):
    global last
    answer = 0

    jobs.sort()

    Q = []
    start = -1
    end = 0
    cnt = 0
    length = len(jobs)
    j = 0

    while cnt < length:

        for i in range(j, length):
            if start < jobs[i][0] <= end:
                heapq.heappush(Q, (jobs[i][1], jobs[i][0]))
            else:
                j = i
                break

        if Q:
            current = heapq.heappop(Q)
            request = current[1]
            start = end
            end = start + current[0]
            answer += end - request
            cnt += 1

        else:
            end += 1

    return answer // length


j = [[0, 3], [1, 9], [2, 6]]
print(solution(j))
