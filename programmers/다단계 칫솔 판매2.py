def solution(enroll, referral, seller, amount):
    d = {}
    d_money = {}

    len_enroll = len(enroll)
    for i in range(len_enroll):
        d[enroll[i]] = referral[i]

    len_seller = len(seller)
    for i in range(len_seller):
        profit = amount[i] * 100
        d_money[seller[i]] = d_money.setdefault(seller[i], 0) + profit
        e = seller[i]
        r = d[e]
        distribution = profit // 10
        while r != "-" and distribution != 0:
            d_money[e] -= distribution
            d_money[r] = d_money.setdefault(r, 0) + distribution
            distribution //= 10
            e = r
            r = d[e]

        d_money[e] -= distribution

    answer = []
    for name in enroll:
        try:
            answer.append(d_money[name])
        except KeyError:
            answer.append(0)

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-",     "-",   "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
