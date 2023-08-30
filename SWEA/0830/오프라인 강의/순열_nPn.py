# nPn
def perm(n, k): # n은 원소갯수, k: depth
    if n == k:
        print(p)
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k+1)
                visited[i] = 0


# a = [1, 2, 3]
# N = len(a)
# p = [0] * N
# visited = [0] * N
# perm(N, 0)

# 고정하는 방법
a = [1, 2, 3, 4]
N = len(a)
p = [0] * (N + 1)
p[0] = p[N] = a[0]
visited = [0] * N
visited[0] = 1
perm(N, 1)

