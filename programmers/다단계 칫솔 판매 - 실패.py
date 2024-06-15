# 각 단계에서 전부 내림 해야 되는데 나는 걍 다 합친 다음에 내림해서 틀림

def solution(enroll, referral, seller, amount):
    d = {}

    len_seller = len(seller)
    for i in range(len_seller):
        d[seller[i]] = d.setdefault(seller[i], 0) + amount[i] * 100

    len_enroll = len(enroll)
    for i in range(len_enroll - 1, -1, -1):
        distribution = int(d.setdefault(enroll[i], 0) * 0.1)
        d[enroll[i]] -= distribution
        d[referral[i]] = d.setdefault(referral[i], 0) + distribution

    answer = []
    for name in enroll:
        answer.append(d[name])

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-",     "-",   "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
print(solution(["john", "mary", "edward", "sam"],
               ["-", "-", "-", "-"],
               ["john", "mary", "edward", "sam"],
               [1, 1, 1, 1]))
print(solution(["john", "mary", "edward", "sam", "emily"],
               ["-", "john", "mary", "edward", "sam"],
               ["john", "mary", "edward", "sam", "emily"],
               [1, 1, 1, 1, 1]))
