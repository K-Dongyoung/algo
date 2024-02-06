import sys
sys.stdin = open('forth.txt')


def cal(arr, L):
    stack = [0] * L
    top = -1
    for c in arr:
        if c not in '+-*/.':    #피연산자인 경우
            top += 1
            stack[top] = int(c)
        elif c in '+-*/':   # 연산자인 경우
            if top < 1:
                return 'error'
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
                    stack[top] = op1 // op2
        elif c == '.':
            if top == 0:
                return stack[top]
            else:
                return 'error'


T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    L = len(arr)
    print(f'#{tc} {cal(arr, L)}')