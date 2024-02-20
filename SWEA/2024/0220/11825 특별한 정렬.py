import sys

sys.stdin = open("input2.txt")

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N // 2):
        max_index = N - 1
        min_index = N - 1
        for j in range(2 * i, N):
            if arr[max_index] < arr[j]:
                max_index = j
            if arr[min_index] > arr[j]:
                min_index = j

        if max_index == 2 * i + 1:
            max_index = min_index

        arr[2 * i + 1], arr[min_index] = arr[min_index], arr[2 * i + 1]
        if i == N // 2 - 1:
            continue
        arr[2 * i], arr[max_index] = arr[max_index], arr[2 * i]

    print(f"#{tc}", end=" ")
    for i in range(10):
        print(arr[i], end=" ")
    print()
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        index = i
        for j in range(i+1, N):
            if i % 2 == 0:
                if arr[j] > arr[index]:
                    index = j

            else:
                if arr[j] < arr[index]:
                    index = j

        arr[i], arr[index] = arr[index], arr[i]

    print(f"#{tc}", end=" ")
    for i in range(10):
        print(arr[i], end=" ")
    print()
