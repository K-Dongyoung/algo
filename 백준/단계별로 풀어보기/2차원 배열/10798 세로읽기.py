arr = [list(input()) for _ in range(5)]
cnt = 15
while cnt:
    for i in range(5):
        if arr[i]:
            print(arr[i].pop(0), end='')
    cnt -= 1

arr = [list(input()) for _ in range(5)]
for j in range(15):
    for i in range(5):
        try:
            print(arr[i][j], end='')
        except:
            continue