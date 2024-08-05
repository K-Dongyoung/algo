def solution(s):
    cnt = 0
    cnt_0 = 0

    while s != "1":
        cnt_1 = 0

        for n in s:
            if n == "1":
                cnt_1 += 1
            else:
                cnt_0 += 1

        new_s = ""
        while cnt_1 > 1:
            quotient = cnt_1 // 2
            remainder = cnt_1 % 2
            new_s += str(remainder)
            cnt_1 = quotient
        new_s += str(1)
        s = new_s
        cnt += 1

    return [cnt, cnt_0]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
