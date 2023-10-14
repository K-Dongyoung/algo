def dfs(n, lst, sum):
    if n == N:
        if sum == 0:
            ans.append(lst)
        return
    dfs(n+1, lst + [arr[n]], sum + arr[n])
    dfs(n+1, lst, sum)



arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
ans = []
dfs(0, [], 0)
print(*ans)