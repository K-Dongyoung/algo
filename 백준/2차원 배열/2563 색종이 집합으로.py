N = int(input())
S = set()
for _ in range(N):
    x, y = map(int, input().split())
    for i in [a for a in range(x, x+10)]:
        for j in [b for b in range(y, y+10)]:
            S.add((i, j))
print(len(S))
