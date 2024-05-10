import heapq
def solution(jobs):

    Q = []
    for i in range(len(jobs)):
        heapq.heappush(Q, jobs[i])

    return Q




j = [[0, 3], [1, 9], [2, 6]]
print(solution(j))
