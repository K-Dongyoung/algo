import sys
sys.stdin = open('Indonesia.txt')

def prim(start):
    D[start] = 0
    # 최소 가중치 찾기
    for _ in range(N):
        min_v = 1_500_000

        for i in range(1, N+1):
            if not visited[i] and D[i] < min_v:
                min_v = D[i]
                # 정점 선택
                v = i
        # visited
        visited[v] = 1
        # 가중치 갱신
        for w in range(1, N+1):
            if not visited[w]:
                d = ((X[v]-X[w])**2 + (Y[v]-Y[w])**2)**0.5
                if D[w] > d:
                    D[w] = d
                    PI[w] = v


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = [0] + list(map(int, input().split()))
    Y = [0] + list(map(int, input().split()))
    E = float(input())
    # visited
    visited = [0] * (N+1)
    # D
    D = [1_500_000] * (N+1)
    # PI
    PI = list(range(N+1))

    prim(1)
    result = 0
    for i in range(1, N+1):
        result += E * D[i]**2

    print(f'#{tc} {result: .0f}')
