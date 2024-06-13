N = int(input())
numbers = list(map(int, input().split()))
answer = 0

for number in numbers:
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
            if count > 2:
                break
    if count == 2:
        answer += 1

print(answer)
