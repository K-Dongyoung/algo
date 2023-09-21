import sys
sys.stdin = open('group.txt')
def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union(a, b):
    x = find_set(a)
    y = find_set(b)

    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = list(range(N+1))
    set1 = set()

    for i in range(M):
        union(arr[2*i], arr[2*i+1])

    for n in parent:
        set1.add(find_set(n))
    set1.remove(0)

    print(f'#{tc} {len(set1)}')