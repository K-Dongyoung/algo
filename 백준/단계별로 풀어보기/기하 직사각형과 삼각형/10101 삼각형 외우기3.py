data = [int(input()) for _ in range(3)]
data_set = set(data)

if sum(data) != 180:
    print("Error")

elif len(data_set) == 1:
    print("Equilateral")

elif len(data_set) == 2:
    print("Isosceles")

elif len(data_set) == 3:
    print("Scalene")
