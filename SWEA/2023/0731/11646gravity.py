T = int(input())

for n in range(T):
    N = int(input())
    L = []
    L = list(map(int, input().split()))
    max_height = -1
    for i in range(len(L)):
        height = (len(L) - 1) - i
        for j in range(i + 1, len(L)):
            if L[i] <= L[j]:
                height -= 1
        if height > max_height:
            max_height = height
    print(f'#{n+1} {max_height}')
