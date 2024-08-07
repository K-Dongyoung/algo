import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    dump = int(input())
    height = list(map(int, input().split()))

    count = [0] * 101
    max_i = 1
    min_i = 100
    answer = -1

    for i in range(100):
        count[height[i]] += 1
        if max_i <= height[i]:
            max_i = height[i]
        if min_i >= height[i]:
            min_i = height[i]

    while dump > 0:
        count[max_i] -= 1
        count[min_i] -= 1
        count[max_i - 1] += 1
        count[min_i + 1] += 1
        dump -= 1
        if count[max_i] == 0:
            max_i -= 1
        if count[min_i] == 0:
            min_i += 1

    answer = max_i - min_i

    print(f"#{tc} {answer}")