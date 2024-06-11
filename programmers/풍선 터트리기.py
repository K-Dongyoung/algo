def solution(a):
    answer = 2
    a_len = len(a)

    if a_len < 3:
        return a_len

    left = a[:]
    right = a[:]
    for i in range(a_len):
        if i - 1 >= 0:
            left[i] = min(left[i - 1], left[i])
        if a_len - i < a_len:
            right[a_len - i - 1] = min(right[a_len - i], right[a_len - i - 1])

    for i in range(1, a_len - 1):
        if a[i] > left[i - 1] and a[i] > right[i + 1]:
            continue
        answer += 1

    return answer


print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
