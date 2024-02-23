import sys
sys.stdin = open("sample_input.txt")

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    count = 0

    for i in range(1 << len(A)):
        subset_sum = 0
        temp = []
        for j in range(len(A)):
            if i & (1 << j):
                subset_sum += A[j]
                temp.append(A[j])
        if subset_sum == K and len(temp) == N:
            count += 1

    print(f"#{tc} {count}")
