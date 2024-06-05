def solution(sequence):
    sequence_len = len(sequence)
    max_sum = -100000 * sequence_len
    sequence_a = [sequence[k] * (k % 2) * (-1) + sequence[k] * ((k + 1) % 2) for k in range(sequence_len)]
    sequence_b = [sequence[k] * ((k + 1) % 2) * (-1) + sequence[k] * (k % 2) for k in range(sequence_len)]
    for i in range(sequence_len):
        subset_len = sequence_len - i
        for j in range(i + 1):
            max_sum = max(max_sum, sum(sequence_a[j:j + subset_len]), sum(sequence_b[j:j + subset_len]))

    return max_sum


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))