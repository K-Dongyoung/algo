from collections import deque


def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for w in graph[v]:
        if visited[w] == 0:
            dfs(w)


def bfs(v):
    visited = [0] * (N + 1)
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        cv = queue.popleft()
        print(cv, end=" ")
        for w in graph[cv]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[cv] + 1


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for l in graph:
    l.sort()

visited = [0] * (N + 1)
dfs(V)
print()

bfs(V)

"""
4 5 1
1 2
1 3
1 4
2 4
3 4

"""
