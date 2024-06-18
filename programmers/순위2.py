from collections import deque


def solution(n, results):
    answer = 0

    def bfs(num, l_pc):
        cnt = 0
        q = deque()
        q.append(num)
        visited = [0] * (n + 1)
        visited[num] = 1
        while q:
            v = q.popleft()
            for item in l_pc[v]:
                if visited[item] == 0:
                    q.append(item)
                    visited[item] = 1
                    cnt += 1
        return cnt

    p = [[] for _ in range(n + 1)]
    c = [[] for _ in range(n + 1)]

    for w, l in results:
        p[l].append(w)
        c[w].append(l)

    for i in range(1, n + 1):
        up = bfs(i, p)
        down = bfs(i, c)
        if up + down == n - 1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
