M = int(input())
N = int(input())

numbers = [i for i in range(N + 1)]
numbers[1] = 0

for i in range(2, int(N ** 0.5) + 1):  # 100이 소수인지 아닌지는 2부터 10까지만 나눠 보면 됨.
    if numbers[i] > 0:                 # 11로 나누면 몫이 10보다 작을 것이고 그것은 10까지 나눌 때 전부 고려됨
        for j in range(i * i, N + 1, i):  # 5 * 5부터 고려해도 되는 이유 : 5 * 2 ~ 5 * 4는 2 ~ 4에서 이미 고려됨
            numbers[j] = 0

prime = [i for i in range(M, N + 1) if numbers[i] > 0]

s = sum(prime)
if s == 0:
    print(-1)
else:
    print(s)
    print(prime[0])
