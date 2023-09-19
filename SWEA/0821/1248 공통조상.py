import sys
sys.stdin = open('ancestor.txt')

def find_ancestor(a, b):
    A = []
    B = []
    result = 0
    while tree[a][2]:
        A.append(tree[a][2])
        a = tree[a][2]
    while tree[b][2]:
        B.append(tree[b][2])
        b = tree[b][2]
    for i in A:
        for j in B:
            if i == j:
                result = i
                return result

def preorder(n):
    global count
    if n:
        count += 1
        preorder(tree[n][0])
        preorder(tree[n][1])


T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    temp = list(map(int, input().split()))

    tree = [[0]*3 for _ in range(V+1)]
    for i in range(E):
        p = temp[i*2]
        c = temp[i*2+1]
        tree[c][2] = p
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c

    count = 0
    ancestor = find_ancestor(n1, n2)
    preorder(ancestor)
    print(f'#{tc} {ancestor} {count}')