# 주석은 다른 사람 풀이
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
        # cnt_1 = s.count("1")
        # cnt_0 += len(s) - cnt_1

        new_s = ""
        while cnt_1 > 0:
            quotient = cnt_1 // 2
            remainder = cnt_1 % 2
            new_s += str(remainder)
            cnt_1 = quotient
        s = new_s
        # s =bin(cnt_1)[2:]

        cnt += 1

    return [cnt, cnt_0]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
