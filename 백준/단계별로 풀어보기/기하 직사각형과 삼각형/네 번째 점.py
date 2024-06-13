dx = {}
dy = {}
for i in range(3):
    x, y = map(int, input().split())
    dx[x] = dx.setdefault(x, 0) + 1
    dy[y] = dy.setdefault(y, 0) + 1

for k, v in dx.items():
    if v == 1:
        X = k

for k, v in dy.items():
    if v == 1:
        Y = k

print(X, Y)
