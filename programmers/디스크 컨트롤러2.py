import heapq

def solution(jobs):
    global last
    answer = 0

    Q = []
    start = 0
    end = 0
    cnt = 0
    length = len(jobs)

    while cnt < length:

        for job in jobs:
            if len(job) == 2 and start <= job[0] <= end:
                heapq.heappush(Q, (job[1], job[0]))
                job.append(1)

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
