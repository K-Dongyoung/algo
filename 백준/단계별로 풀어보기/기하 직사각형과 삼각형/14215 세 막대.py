data = sorted(list(map(int, input().split())))
a = data[0] + data[1]
if a > data[2]:
    print(sum(data))

else:
    print(2 * a - 1)
