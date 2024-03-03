def brute_force(text, pattern):
    len_p = len(pattern)
    len_t = len(text)

    if len_p > len_t:
        return False

    t_idx = p_idx = 0
    while t_idx < len_t and p_idx < len_p:
        if text[t_idx] != pattern[p_idx]:
            t_idx -= p_idx
            p_idx = -1
        t_idx += 1
        p_idx += 1

    if p_idx == len_p:
        return t_idx - len_p


t = "this is a book~!"
p = "is"
print(brute_force(t, p))