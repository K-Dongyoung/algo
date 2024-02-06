import sys
sys.stdin = open('ptest.txt')

def f(string):
    stack = [0] * len(string)
    top = -1
    for c in string:
        if c == '(':
            top += 1
            stack[top] = c
        elif c == '[':
            top += 1
            stack[top] = c
        elif c == ')':
            if top == -1:
                return 0
            elif stack[top] != '(':
                return 0
            else:
                top -= 1
        elif c == ']':
            if top == -1:
                return 0
            elif stack[top] != '[':
                return 0
            else:
                top -= 1
    if top != -1:
        return 0
    return 1



T = int(input())
for tc in range(1, T+1):
    code = input()
    print(f'#{tc} {f(code)}')