def solution(sequence):
    sequence_len = len(sequence)
    max_sum = -100000 * sequence_len
    sequence_a = [sequence[k] * (k % 2) * (-1) + sequence[k] * ((k + 1) % 2) for k in range(sequence_len)]

    for i in range(sequence_len):
        subset_len = sequence_len - i
        subset_sum_a = sum(sequence_a[:subset_len])
        max_sum = max(max_sum, abs(subset_sum_a))
        for j in range(1, i + 1):
            subset_sum_a = subset_sum_a - sequence_a[j - 1] + sequence_a[j + subset_len - 1]
            max_sum = max(max_sum, abs(subset_sum_a))

    return max_sum


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
