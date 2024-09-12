def solution(s):
    l = list(map(int, s.split()))
    return f"{min(l)} {max(l)}"


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
