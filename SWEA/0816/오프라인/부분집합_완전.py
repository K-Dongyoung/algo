def powerset(n, k):
    global count, total
    total += 1
    if k == n:
        sum = 0
        for i in range(n):
            if bit[i]:
                sum += arr[i]
        if sum == 10:
            count += 1
            for i in range(n):
                if bit [i]:
                    print(arr[i], end=' ')
            print()

    else:
        bit[k] = 1
        powerset(n, k + 1)
        bit[k] = 0
        powerset(n, k + 1)
        return


count = 0
total = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
bit = [0] * N
powerset(N, 0)
print(f'count = {count}, 호출횟수 = {total}')
