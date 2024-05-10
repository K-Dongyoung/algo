def solution(jobs):
    global last
    answer = 0
    L = len(jobs)

    jobs.sort()

    now = 0
    start = 0

    return answer


def enq(v):
    global last
    last += 1
    heap[last] = v
    c = last
    p = c // 2
    while p > 0 and heap[p][1] > heap[c][1]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def deq():
    global last
    result = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c + 1] > heap[c]:
            c += 1
        if heap[p][1] > heap[c][1]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2

    return result


heap = [0] * 501
last = 0
j = [[0, 5], [1, 2], [5, 5], [6, 2], [7, 1]]
print(solution(j))
