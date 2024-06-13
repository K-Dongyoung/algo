N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
prime = []
i = 0

for n in range(2, 1001):
    flag = True
    for p in prime:
        if n % p == 0:
            flag = False
            break

    if flag:
        while i < N:
            if n > numbers[i]:
                i += 1
            elif n == numbers[i]:
                answer += 1
                i += 1
                break
            else:
                break

        prime.append(n)

    if i == N:
        break

print(answer)
