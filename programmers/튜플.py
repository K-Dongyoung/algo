def solution(s):
    s = s[1:-1]
    answer = []
    a = list()
    b = ""

    for c in s:
        if c != "{" and c != "}":
            b += c
        elif c == "}":
            a.append(set(map(int, b.split(','))))
        elif c == "{":
            b = ""

    a.sort(key=lambda x: len(x))

    prev_s = set()
    for si in a:
        n = next(iter(si - prev_s))
        prev_s = si
        answer.append(n)

    return answer


def solution2(s):
    answer = []
    a = s.lstrip('{').rstrip('}').split('},{')
    b = []
    for c in a:
        b.append(set(map(int, c.split(","))))

    b.sort(key=len)

    prev_s = set()
    for si in b:
        n = next(iter(si - prev_s))
        prev_s = si
        answer.append(n)

    return answer


print(solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution2("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution2("{{20,111},{111}}"))
print(solution2("{{123}}"))
print(solution2("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
