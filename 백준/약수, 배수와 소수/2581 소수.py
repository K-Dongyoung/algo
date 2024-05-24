M = int(input())
N = int(input())
answer = []

for n in range(M, N + 1):
    if n == 1:
        continue
    flag = True
    for i in range(2, n//2 + 1):
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
