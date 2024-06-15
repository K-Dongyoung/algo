def solution(enroll, referral, seller, amount):
    d = {}
    len_enroll = len(enroll)
    answer = [0] * len_enroll

    for i in range(len_enroll):
        d[enroll[i]] = (referral[i], i)

    len_seller = len(seller)
    for i in range(len_seller):
        profit = amount[i] * 100
        e = seller[i]
        r = d[e][0]
        answer[d[e][1]] += profit
        distribution = profit // 10
        while r != "-" and distribution != 0:
            answer[d[e][1]] -= distribution
            answer[d[r][1]] += distribution
            distribution //= 10
            e = r
            r = d[e][0]

        answer[d[e][1]] -= distribution

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-",     "-",   "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
