def solution(s):
    answer = 0
    length = len(s)
    a = s + s[:length - 1]
    for i in range(length):
        if is_right_parentheses(a[i:i + length]):
            answer += 1
    return answer


def is_right_parentheses(string):
    stack = []
    i = -1
    d = {"(": ")", "{": "}", "[": "]"}

    for s in string:
        if s in d.keys():
            stack.append(s)
            i += 1
        elif s in d.values():
            if not stack:
                return False
            else:
                if s == d[stack[i]]:
                    stack.pop()
                    i -= 1
                else:
                    return False

    if stack:
        return False

    return True


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
