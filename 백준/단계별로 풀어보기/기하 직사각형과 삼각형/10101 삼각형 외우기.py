a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")

elif a == b == c:
    print("Equilateral")

elif a == b and a != c:
    print("Isosceles")

elif b == c and b != a:
    print("Isosceles")

elif a == c and a != b:
    print("Isosceles")

else:
    print("Scalene")
