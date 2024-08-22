def solution(clothes): # 시간 초과
    d = {}
    for c in clothes:
        d[c[1]] = d.setdefault(c[1], 0) + 1
    len_d = len(d)
    return f(list(d.values()), 1, 0, len_d) - 1

def f(l, a, s, e):
    if s < e:
        return f(l, a * l[s], s + 1, e) + f(l, a, s + 1, e)
    elif s == e:
        return a



# def solution2(clothes):
    # ans = 0
    # d = {}
    # for c in clothes:
    #     d[c[1]] = d.setdefault(c[1], 0) + 1
    # len_d = len(d)





print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
