def powerset(N, k):
    if k == N:
        print(bit, end=' ')
        for i in range(N):
            if bit[i]:
                print(arr[i], end=' ')
        print()
        return
    else:
        bit[k] = 1
        powerset(N, k + 1)
        bit[k] = 0
        powerset(N, k + 1)
        return

arr = [1, 2, 3]
bit = [0] * 3
powerset(3, 0)
