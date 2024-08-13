def solution(want, number, discount):
    discount_len = len(discount)
    start_i = 0
    ans = 0

    while start_i + 10 <= discount_len:
        d = dic(want, number)
        discount_i = start_i

        flag = True
        for i in range(discount_i, discount_i + 10):
            if d.get(discount[i], -1) == -1:
                flag = False
                start_i = i + 1
                break
            elif d.get(discount[i], -1) == 0:
                flag = False
                start_i += 1
                break
            elif d.get(discount[i], -1) > 0:
                d[discount[i]] -= 1

        if flag:
            ans += 1
            start_i += 1

    return ans


def dic(want, number):
    d = {}
    for i in range(len(want)):
        d[want[i]] = number[i]
    return d


print(solution2(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution2(["banana", "apple", "rice", "pork", "chicken"], [2, 3, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution2(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
print(solution2(["banana"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
