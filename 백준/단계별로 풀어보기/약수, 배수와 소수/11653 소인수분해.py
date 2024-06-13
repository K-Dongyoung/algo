def f(n):
    if n == 1:
        return

    numbers = [1] * (int(N ** 0.5) + 1)

    for i in range(2, int(N ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, N + 1, i):
                numbers[j] = 0

    prime = [i for i in range(2, N + 1) if numbers[i] == 1]

    i = 0
    while n > 1:
        d = prime[i]
        r = n % d
        if r == 0:
            print(d)
            n //= d
        else:
            i += 1


N = int(input())
f(N)
