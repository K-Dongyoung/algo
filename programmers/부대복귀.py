from collections import deque


def solution(n, roads, sources, destination):
    answer = []

    adj = [[] for _ in range(n + 1)]
    for road in roads:
        adj[road[0]].append(road[1])
        adj[road[1]].append(road[0])

    visited = [0] * (n + 1)
    q = deque()

    q.append(destination)
    visited[destination] = 1

    while q:
        v = q.popleft()
        for w in adj[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

    for source in sources:
        if source == 0:
            answer.append(-1)
        else:
            answer.append(visited[source] - 1)

    return answer


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
