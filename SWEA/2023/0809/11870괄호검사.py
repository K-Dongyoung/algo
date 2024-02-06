import sys
sys.stdin = open('괄호검사.txt')

L = ['(', '[', '{']
R = [')', ']', '}']
size = 10000

def p_check(code):
    stack = [0] * size
    top = -1
    for c in code:
        for i in range(3):
            if c == R[i] and top == -1:
                return 0
            if c == L[i]:
                top += 1
                stack[top] = c
            if c == R[i]:
                temp = stack[top]
                top -= 1
                if temp != L[i]:
                    return 0
    if top != -1:
        return 0
    return 1


T = int(input())
for tc in range(1, T+1):

    code = input()
    result = p_check(code)

    print(f'#{tc} {result}')




