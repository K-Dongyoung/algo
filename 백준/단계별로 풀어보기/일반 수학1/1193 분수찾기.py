X = int(input())
level = 1
ceiling = 1

while X > ceiling:
    level += 1
    ceiling += level

floor = ceiling - level + 1
n = X - floor

if level % 2 == 0:
    row = 1 + n
    col = level - n
else:
    row = level - n
    col = 1 + n

print(f"{row}/{col}")
