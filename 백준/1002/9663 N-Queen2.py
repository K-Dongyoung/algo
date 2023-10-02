def dfs(k, lst):
    global cnt
    if k == N:
        cnt += 1
        return

    temp = list(range(N))
    for ki, idx in lst:
        i1 = idx - (k-ki)
        i2 = idx
        i3 = idx + (k-ki)
        temp[i2] = -1
        if 0 <= i1 < N:
            temp[i1] = -1
        if 0 <= i3 < N:
            temp[i3] = -1

    for i in temp:
        if i >= 0:
            dfs(k+1, lst+[(k, i)])


N = int(input())
cnt = 0
dfs(0, [])
print(cnt)
