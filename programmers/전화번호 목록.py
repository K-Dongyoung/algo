def solution1(phone_book):
    phone_book.sort(key=lambda x: (len(x), x))
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                return False
    return True


def solution(phone_book):
    return f(phone_book, 0)

def f(p_list, i):
    h = [[] for _ in range(10)]
    for n in p_list:
        if i < len(n):
            h[int(n[i])].append(n)

    for s in h:
        if len(s) <= 1:
            continue
        s.sort(key=len)
        if len(s[0]) <= i + 1:
            return False
        elif len(s[0]) > i + 1:
            return f(s, i + 1)
    return True


def gpt_code(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["123", "1231"]))
print(solution(["1234567890", "12", "1"]))