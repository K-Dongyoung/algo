arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
result = []

for i in range(1<<len(arr)):
    subset = []
    sum = 0
    for j in range(len(arr)):
        if i & (1<<j):
            subset.append(arr[j])
            sum += arr[j]
    if sum == 0:
        result.append(subset)
print(*result)