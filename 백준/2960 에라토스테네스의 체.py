def f(n, k):
    numbers = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if numbers[i] > 0:
            for j in range(i, n + 1, i):
                if numbers[j] > 0:
                    numbers[j] = 0
                    k -= 1
                if k == 0:
                    return j

# def f2(n, k):
#     numbers = [i for i in range(n + 1)]
#     for i in range(2, n + 1):
#         if numbers[i] > 0:
#             numbers[i] = 0
#             k -= 1
#             if k == 0:
#                 return i
#             for j in range(i * i, n + 1, i):
#                 if numbers[j] > 0:
#                     numbers[j] = 0
#                     k -= 1
#                     if k == 0:
#                         return j


N, K = map(int, input().split())
print(f(N, K))
