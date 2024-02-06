import sys
sys.stdin = open('password.txt')

T = 10
for tc in range(1, T+1):
    N, password = input().split()
    N = int(N)
    stack = [0] * N
    top = -1

    for n in password:
        if top == -1:
            top += 1
            stack[top] = n
        else:
            if n != stack[top]:
                top += 1
                stack[top] = n
            else:
                top -= 1

    ans = ''.join(stack[:top+1])
    print(f'#{tc} {ans}')