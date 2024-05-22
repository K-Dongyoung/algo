N = int(input())
a = 4
for i in range(N):
    a += (2 ** i) * ((2 ** i) + 1) * 2 + (2 ** i) ** 2

print(a)
