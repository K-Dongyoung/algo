import sys
a = sys.stdin.read

"""
입력값이 다음가 같을 때
50
60
70
a()는  "50\n60\n70\n" 가 된다.
"""

data = list(map(int, a().strip().split()))
data_set = set(data)

if sum(data) != 180:
    print("Error")

elif len(data_set) == 1:
    print("Equilateral")

elif len(data_set) == 2:
    print("Isosceles")

elif len(data_set) == 3:
    print("Scalene")
