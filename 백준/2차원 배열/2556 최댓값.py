arr = [list(map(int, input().split())) for _ in range(9)]
mi = 0
mj = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > arr[mi][mj]:
            mi = i
            mj = j
print(arr[mi][mj])
print(mi+1, mj+1)