# 조합
def comb(n, r, p):
    if r == 0:
        print(p)
        return
    elif n < r:
        return
    else:

        comb(n-1, r-1, p + [arr[]])
        comb(n-1, r, p)






arr = [3, 4, 5, 6]
K = 3
# p = [0] * K
# visited = [0] * len(arr)
comb(len(arr), K, [])








# 순열
# def perm(k, n, p):
#     if k == n:
#         print(p)
#         return
#     for i in range(n):
#         # if not visited[i]:
#         #     visited[i] = 1
#             perm(k+1, n, p + [arr[i]])
#             # visited[i] = 0
#
#
# arr = [3, 4, 5, 6]
# visited = [0] * len(arr)
# perm(0, 3, [])