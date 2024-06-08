# 블로그 참고
def solution(sequence):
    sequence_len = len(sequence)
    max_sum = -100000 * sequence_len
    sum_a = 0
    sum_b = 0
    subset_a_min = 0
    subset_b_min = 0
    pulse = 1

    for i in range(sequence_len):
        sum_a += sequence[i] * pulse
        sum_b += sequence[i] * (-pulse)

        max_sum = max(max_sum, sum_a - subset_a_min, sum_b - subset_b_min)

        subset_a_min = min(subset_a_min, sum_a)
        subset_b_min = min(subset_b_min, sum_b)

        pulse *= -1

    return max_sum


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
