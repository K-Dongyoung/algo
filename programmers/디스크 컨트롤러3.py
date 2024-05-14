def solution(jobs):
    global last
    answer = 0

    start = 0
    end = 0
    cnt = 0
    length = len(jobs)

    while cnt < length:

        for job in jobs:
            if len(job) == 2 and start <= job[0] <= end:
                enq(job)
                job.append(1)

        if last >= 1:
            current = deq()
            request = current[0]
            start = end
            end = start + current[1]
            answer += end - request
            cnt += 1

        else:
            end += 1
            start = end

    return answer // length


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
j = [[0, 3], [1, 9], [2, 6]]
print(solution(j))
