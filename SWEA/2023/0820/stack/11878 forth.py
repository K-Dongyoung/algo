import sys
sys.stdin = open('forth.txt')

def cal(code):
    stack = []
    for c in code:
        if c.isdigit():
            stack.append(int(c))
        elif c == '.':
            if len(stack) != 1:
                return 'error'
            else:
                return stack.pop()
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


T = int(input())
for tc in range(1, T+1):
    code = list(input().split())
    print(f'#{tc} {cal(code)}')