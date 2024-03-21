import sys
sys.stdin = open("sample_input.txt")

d = {')': '(', '}': '{'}


def p_check(s):
    stack = []
    for c in string:
        if c == '(' or c == '{':
            stack.append(c)
        elif c == '}' or c == ')':
            if not stack or stack.pop() != d[c]:
                return 0
    if stack:
        return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    string = input()
    print(f'#{tc} {p_check(string)}')


"""
def p_check(s):
    stack = []
    for c in string:
        if c == '(' or c == '{':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return 0
            elif stack[-1] == '{':
                return 0
            elif stack[-1] == '(':
                stack.pop()
        elif c == '}':
            if len(stack) == 0:
                return 0
            elif stack[-1] == ')':
                return 0
            elif stack[-1] == '{':
                stack.pop()
    if len(stack) != 0:
        return 0
    return 1
"""