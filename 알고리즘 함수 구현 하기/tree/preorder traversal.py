"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

"""


def preorder(v):
    if v:
        print(v)
        for c in tree[v]:
            preorder(c)


V = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(V + 1)]

for i in range(len(arr) // 2):
    tree[arr[2 * i]].append(arr[2 * i + 1])
print(tree)

preorder(1)