import sys
sys.stdin = open('cal3.txt')

def conversion(string):
    result = ''
    stack = [0] * len(string)
    top = -1
    for c in string:
        if c.isdigit():
            result += c
        elif c == ')':
            while stack[top] != '(':
                result += stack[top]
                top -= 1
            top -= 1
        else:
            if top > -1:
                while icp[c] <= isp[stack[top]]:
                    result += stack[top]
                    top -= 1
                    if top == -1:
                        break
            top += 1
            stack[top] = c
    while top > -1:
        result += stack[top]
        top -= 1
    return result

def cal(string):
    stack = [0] * len(string)
    top = -1
    for c in string:
        if c.isdigit():
            top += 1
            stack[top] = int(c)
        else:
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            if c == '+':
                top += 1
                stack[top] = op1 + op2
            elif c == '-':
                top += 1
                stack[top] = op1 - op2
            elif c == '*':
                top += 1
                stack[top] = op1 * op2
            elif c == '/':
                top += 1
                stack[top] = op1 / op2
    return stack[top]

icp = {'(':3, '+':1, '-':1, '*':2, '/':2}
isp = {'(':0, '+':1, '-':1, '*':2, '/':2}

T = 10
for tc in range(1, T+1):
    N = int(input())
    string = input()
    print(f'#{tc} {cal(conversion(string))}')