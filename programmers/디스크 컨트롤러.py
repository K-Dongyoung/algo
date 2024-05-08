def solution(jobs):
    global last
    answer = 0
    L = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    last += 1
    heap[last] = jobs[0]
    s = 0
    k = 1
    for i in range(L):
        current = heap[1]
        heap[1] = heap[last]
        last -= 1
        p = 1
        c = p * 2
        while c <= last:
            if c + 1 <= last and heap[c][1] < heap[c + 1][1]:
                c += 1
            if heap[p][1] > heap[c][1]:
                heap[p], heap[c] = heap[c], heap[p]
                p = c
                c = p * 2
        e = (s + current[1])
        for j in range(k, L):
            if s <= jobs[j][0] <= e:
                last += 1
                heap[last] = jobs[j]
                c = last
                p = c // 2
                while p > 0 and heap[p][1] > heap[c][1]:
                    heap[p], heap[c] = heap[c], heap[p]
                    c = p
                    p = c // 2
            else:
                k = j
                break

        answer += e - current[0]
        s = e

    answer /= L

    return answer



heap = [0] * 501
last = 0
j = [[0, 5], [1, 2], [5, 5], [6, 2], [7, 1]]
print(solution(j))
