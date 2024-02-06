import sys
sys.stdin = open('subtree.txt')

def preorder(n):
    global count
    if n:
        count += 1
        preorder(tree[n][0])
        preorder(tree[n][1])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))

    tree = [[0] * 3 for _ in range(E + 2)]
    for i in range(E):
        p = temp[i * 2]
        c = temp[i * 2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    count = 0
    preorder(N)
    print(f'#{tc} {count}')