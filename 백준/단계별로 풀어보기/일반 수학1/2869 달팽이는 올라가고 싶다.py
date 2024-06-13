A, B, V = map(int, input().split())

temp = V - A
day = temp // (A - B)

if temp % (A - B):
    day += 1

print(day + 1)
