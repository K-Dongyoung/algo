N, B = input().split()
B = int(B)
D = 0
for c in N:
    if c.isdigit():
        D += int(c)
    else:
        D += ord(c) - ord('A') + 10
    D *= B
D //= B
print(D)