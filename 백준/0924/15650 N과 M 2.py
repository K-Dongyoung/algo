# def comb(n, r, k, lst):
#     if k > n:
#         if len(lst) == r:
#             print(*lst)
#     else:
#         comb(n, r, k+1, lst + [k])
#         comb(n, r, k+1, lst)

def nCr(k, start, lst):
    if k == M:
        print(*lst)
        return
    else:
        for i in range(start, N+1):
            nCr(k+1, i+1, lst+[i])
    pass

N, M = map(int, input().split())
nCr(0, 1, [])
# comb(N, M, 1, [])
