import sys
sys.stdin = open('cal3.txt')


def conversion(C):
    stack = []
    result =''
    for x in C:
        if x.isdigit():
            result += x
        elif x == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            if not stack:
                stack.append(x)
            else:
                if icp[x] > isp[stack[-1]]:
                    stack.append(x)
                else:
                    while stack and icp[x] <= isp[stack[-1]]:
                        result += stack.pop()
                    stack.append(x)
    while stack:
        result += stack.pop()
    return result


def cal(code):
    stack = []
    for c in code:
        if c.isdigit():
            stack.append(int(c))
        else:
            if len(stack) < 2:
                return 'error'
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if c == '+':
                    stack.append(op1 + op2)
                elif c == '-':
                    stack.append(op1 - op2)
                elif c == '*':
                    stack.append(op1 * op2)
                elif c == '/':
                    stack.append(op1 // op2)
    return stack[0]


icp = {'(':3, '+':1, '-':1, '*':2, '/':2}
isp = {'(':0, '+':1, '-':1, '*':2, '/':2}


T = 10
for tc in range(1, T+1):
    N = int(input())
    C = input()
    print(f'#{tc} {cal(conversion(C))}')