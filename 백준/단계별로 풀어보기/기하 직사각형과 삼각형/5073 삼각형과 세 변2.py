import sys
a = sys.stdin.read

data = list(map(int, a().strip().split()))

for i in range(len(data)//3):
    b = sorted(data[3 * i:3 * i + 3])
    if sum(b) == 0:
        break
    if b[0] + b[1] <= b[2]:
        print("Invalid")
    elif len(set(b)) == 1:
        print("Equilateral")
    elif len(set(b)) == 2:
        print("Isosceles")
    elif len(set(b)) == 3:
        print("Scalene")
