import sys
sys.stdin = open('erase_repetition.txt')

T = int(input())
for tc in range(1, T+1):
    string = input()

    size = 10000
    stack = [0] * size
    top = -1

    for c in string:
        if top == -1:
            top += 1
            stack[top] = c
        elif c != stack[top]:
            top += 1
            stack[top] = c
        elif c == stack[top]:
            top -= 1

    count = 0
    for i in range(top+1):
        count += 1

    print(f'#{tc} {count}')

