def solution(s):
    s_len = len(s)
    for i in range(s_len - 1):  # i 1
        sub_len = s_len - i  # sub_len 4
        for j in range(i + 1):  # j 0 ~ 1
            for k in range(j, j + sub_len//2):  # k 0 ~ 1, 1 ~ 2
                if s[k] != s[(sub_len + j - 1) - (k - j)]:
                    break
                if k == j + sub_len//2 - 1:
                    return sub_len
    return 1


print(solution("aaaba"))
