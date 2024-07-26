import heapq


def solution(operations):
    a = []  # 최소 힙
    b = []  # 최대 힙

    for c in operations:
        n = int(c[1:].strip())
        if c[0] == "I":
            heapq.heappush(a, n)
            heapq.heappush(b, -n)

        elif c[0] == "D" and n == 1:
            if a:
                a.remove(-heapq.heappop(b))

        elif c[0] == "D" and n == -1:
            if a:
                b.remove(-heapq.heappop(a))

    if a:
        return [-heapq.heappop(b), heapq.heappop(a)]
    else:
        return [0, 0]


print(solution(["I 1", "I 2", "I 3", "D -1", "D 1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
