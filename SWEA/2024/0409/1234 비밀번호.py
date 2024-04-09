import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T + 1):
    length, num_string = input().split()
    length = int(length)
    stack = [0] * length

    stack[0] = num_string[0]
    top = 0

    for i in range(1, length):
        if stack[top] == num_string[i]:
            top -= 1
        else:
            stack[top + 1] = num_string[i]
            top += 1


    print(f"#{tc} {''.join(stack[:top + 1])}")
