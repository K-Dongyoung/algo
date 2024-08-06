def solution(s):
    stack = []
    i = -1
    for c in s:
        if stack and stack[i] == c:
            stack.pop()
            i -= 1
            continue
        stack.append(c)
        i += 1
    return 1 if not stack else 0


print(solution("baabaa"))
print(solution("cdcd"))
