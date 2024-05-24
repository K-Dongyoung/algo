N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
prime = [2]
i = 0

if numbers[1] == 2:
    answer += 1
    i += 1

for n in range(3, 1001):
    flag = True
    for p in prime:
        if n % p == 0:
            flag = False
            break

    if flag:
        while i < len(numbers):
            if n > numbers[i]:
                i += 1
            elif n == numbers[i]:
                answer += 1
                i += 1
                break

        prime.append(n)

    if i == len(numbers):
        break

print(answer)

"""
시간 초과로 실패
"""
