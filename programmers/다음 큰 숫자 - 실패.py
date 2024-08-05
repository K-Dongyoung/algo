def solution(n):
    a = bin(n)[2:]
    start = len(a) - 1
    end = len(a) - 1
    flag = False
    for i in range(len(a) - 1, -1, -1):
        if a[i] == "1":
            if not flag:
                end = i
                flag = True
            else:
                start = i
        elif a[i] == "0" and flag:
            break

    if start == 0:
        if end == len(a) - 1:
            return int("10" + a[1:], 2)
        else:
            return int(shift_right("10" + a[1:], 2, end + 1), 2)

    else:
        d = list(a)
        d[start - 1], d[start] = d[start], d[start - 1]
        return int(shift_right("".join(d), start + 1, end), 2)


def shift_right(s, start, end):
    a = list(s)
    b = a[start: end + 1]
    c = a[end + 1:]
    d = a[:start]
    e = d + c + b
    return "".join(e)


print(solution(78))
print(solution(15))
print(solution(14))
