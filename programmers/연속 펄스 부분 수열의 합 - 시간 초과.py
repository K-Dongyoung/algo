# 시간 초과로 탈락
def solution(sequence):
    sequence_len = len(sequence)
    max_sum = -100000 * sequence_len
    for i in range(sequence_len):
        subset_len = sequence_len - i
        for j in range(i + 1):
            sum_a = 0
            sum_b = 0
            for k in range(j, j + subset_len):
                sum_a += sequence[k] * (k % 2) * (-1) + sequence[k] * ((k + 1) % 2)
                sum_b += sequence[k] * ((k + 1) % 2) * (-1) + sequence[k] * (k % 2)
                """
                sum_a += sequence[k] * (-1) ** (k % 2)
                sum_b += sequence[k] * (-1) ** ((k + 1) % 2) 이게 더 느림 왜지?
                """
            max_sum = max(max_sum, sum_a, sum_b)

    return max_sum


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
