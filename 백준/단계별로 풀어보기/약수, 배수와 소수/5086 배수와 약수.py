while True:
    a, b = map(int, input().split())

    if (a, b) == (0, 0):
        break

    if a > b and a % b == 0:
        print("multiple")
        continue

    if a < b and b % a == 0:
        print("factor")
        continue

    print("neither")
