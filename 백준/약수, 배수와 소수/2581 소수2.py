M = int(input())
N = int(input())
prime = []
answer = []

for n in range(2, N + 1):
    flag = True
    for p in prime:
        if n % p == 0:
            flag = False
            break

    if flag:
        prime.append(n)
        if n >= M:
            answer.append(n)

if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)
