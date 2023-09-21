import sys
sys.stdin = open('mst.txt')

def prim(start):
    D[start] = 0
    for _ in range(V+1):
        # 최소 가중치 찾기
        min_v = 11
        for i in range(V+1):
            if not visited[i] and D[i] < min_v:
                min_v = D[i]
                # 선택
                v = i
        # 방문 체크
        visited[v] = 1

        # 인접 정점 가중치 갱신
        for n, w in adj[v]:
            if not visited[n] and D[n] > w:
                D[n] = w
                PI[n] = v

    return sum(D)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 리스트
    adj = [[] for _ in range(V+1)]
    # visited
    visited = [0] * (V+1)
    # 가중치 배열
    D = [11] * (V+1)
    # 부모 배열
    PI = list(range(V+1))
    # 인접 리스트 채워서 그래프 만들기
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append((n2, w))
        adj[n2].append((n1, w))

    print(f'#{tc} {prim(0)}')
