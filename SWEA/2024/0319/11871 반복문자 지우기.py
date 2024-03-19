import sys
sys.stdin = open("sample_input.txt")

def push(s, item):
    global top
    top += 1
    if len(s) == top:
        print("full")
        return False
    s[top] = item

def pop(s):
    global top
    if top > -1:
        top -= 1
        return s[top + 1]
    return False

T = int(input())
for tc in range(1, T + 1):
    str_input = input()
    """
    파이썬 방법
    stack = []
    for c in str_input:
        if stack:
            if stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        else:
            stack.append(c)
    print(f'#{tc} {len(stack)}')
    """

    stack = [0] * len(str_input)
    top = -1
    for c in str_input:
        if top > -1:
            if stack[top] != c:
                push(stack, c)
            else:
                pop(stack)
        else:
            push(stack, c)
    print(f'#{tc} {top + 1}')