import sys
sys.stdin = open('erase.txt')

def f(string):
    stack = [0] * len(string)
    top = -1
    for c in string:
        if top == -1:
            top += 1
            stack[top] = c
        else:
            if c == stack[top]:
                top -= 1
            else:
                top += 1
                stack[top] = c
    if top == -1:
        return 0
    else:
        return top + 1


T = int(input())
for tc in range(1, T+1):
    string = input()
    print(f'#{tc} {f(string)}')