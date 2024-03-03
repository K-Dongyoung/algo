def brute_force(t, p):
    len_p = len(p)
    len_t = len(t)

    if len_p > len_t:
        return False

    answer_list = []
    for i in range(len_t - len_p + 1):
        flag = True
        for j in range(len_p):
            if p[j] != t[i + j]:
                flag = False
                break
        if flag:
            answer_list.append(i)
    return answer_list


t = "this is a book~!"
p = "is"
print(brute_force(t, p))