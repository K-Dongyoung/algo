import sys
sys.stdin = open('magnetic.txt')


def s():
    count = 0
    for j in range(length):
        stack = []
        for i in range(length):
            if table[i][j] == 1:
                if not stack:
                    stack.append(1)
            elif table[i][j] == 2:
                if stack:
                    stack.pop()
                    count += 1
    return count

T = 10
for tc in range(1, T+1):
    length = int(input())
    table = [list(map(int, input().split())) for _ in range(length)]
    print(f'#{tc} {s()}')