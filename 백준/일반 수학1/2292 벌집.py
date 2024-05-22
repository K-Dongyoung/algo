N = int(input())
level = 1
answer = 0
ceiling = 1

while True:

    if N <= ceiling:
        answer = level
        break

    ceiling += 6 * level
    level += 1

print(answer)
