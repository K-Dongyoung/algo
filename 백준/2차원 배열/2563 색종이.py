N = int(input())

graph = [[0] * 100 for _ in range(100)]
sum = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if graph[i][j] == 0:
                graph[i][j] = 1
                sum += 1

print(sum)
