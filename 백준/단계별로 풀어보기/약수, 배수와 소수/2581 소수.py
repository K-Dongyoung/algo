M = int(input())
N = int(input())
answer = []

for n in range(M, N + 1):
    if n == 1:
        continue
    flag = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = False
            break

    if flag:
        answer.append(n)

if answer:
    print(sum(answer))
    print(answer[0])

else:
    print(-1)

"""
에라토스테네스의 체 알고리즘 이라고 합니다.. 쩐다..
m = int(input())
n = int(input())
l = [1] * (n + 1)
l[1] = 0

for i in range(2, int(n ** 0.5) + 1):
    if l[i]:
        for j in range(i * i, n + 1, i):
            l[j] = 0

l = [i for i in range(m, n + 1) if l[i] == 1]
if sum(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))
"""
