def solution(enroll, referral, seller, amount):
    d = {}  # 판매원과 추천인 매칭하는 사전 만들기
    d_money = {}  # 각 구성원들에게 돌아가는 이익 저장할 사전

    len_enroll = len(enroll)  # 판매원과 추천인 매칭하는 사전 만들기
    for i in range(len_enroll):
        d[enroll[i]] = referral[i]

    len_seller = len(seller)  # 각 판매원이 올린 수익 배분 과정
    for i in range(len_seller):
        profit = amount[i] * 100  # 칫솔 팔아 올린 수익
        # 수익 d_money 에 저장
        # seller에 이름이 중복해서 있을 수 있으므로
        d_money[seller[i]] = d_money.setdefault(seller[i], 0) + profit
        # 각 판매원과 추천인
        e = seller[i]
        r = d[e]
        # 판매원의 추천인에게 배분할 금액
        distribution = profit // 10
        # 추천인의 추천인에게 배분하는 과정
        while r != "-" and distribution != 0:
            d_money[e] -= distribution
            d_money[r] = d_money.setdefault(r, 0) + distribution
            distribution //= 10
            e = r
            r = d[e]

        # 민호(center) 까지 배분
        d_money[e] -= distribution

    answer = []
    for name in enroll:
        try:
            answer.append(d_money[name])

        # 판매량이 없는 사람은 d_money에 없으므로
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
