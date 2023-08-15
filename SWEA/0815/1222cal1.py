import sys
sys.stdin = open('cal1.txt')

def conversion(string):
    stack = [0] * 2
    top = -1
    str_result = ''
    for c in string:
        if c == '+':
            if top == -1:
                top += 1
                stack[top] = c
            else:
                str_result += stack[top]
        else:
            str_result += c
    str_result += stack[top]
    return str_result


def cal(string):
    stack = [0] * 2
    top = -1
    for c in string:
        if c not in '+.':    #피연산자인 경우
            top += 1
            stack[top] = int(c)
        elif c == '+':   # 연산자인 경우
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            stack[top] = op1 + op2

    return stack[top]


T = 10
for tc in range(1, T+1):
    length = int(input())
    string = input()
    string_temp = conversion(string)
    print(f'#{tc} {cal(string_temp)}')
