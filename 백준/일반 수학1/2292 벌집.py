N = int(input())
level = 1
ceiling = 1

while N > ceiling:
    ceiling += 6 * level
    level += 1

print(level)
