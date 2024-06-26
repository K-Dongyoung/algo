while True:
    a = list(map(int, input().split()))

    if sum(a) == 0:
        break

    a.sort()
    if a[0] + a[1] <= a[2]:
        print("Invalid")

    elif len(set(a)) == 1:
        print("Equilateral")

    elif len(set(a)) == 2:
        print("Isosceles")

    elif len(set(a)) == 3:
        print("Scalene")
