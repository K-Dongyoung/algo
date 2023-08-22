import sys
sys.stdin = open('cal.txt')

def postorder(n):
    # if not tree[n][0] and not tree[n][1]:
    #     return tree[n][3]
    if n:
        a = postorder(tree[n][0])
        b = postorder(tree[n][1])
        if tree[n][3] == '+':
            return a + b
        elif tree[n][3] == '-':
            return a - b
        elif tree[n][3] == '*':
            return a * b
        elif tree[n][3] == '/':
            return a // b
        else:
            return tree[n][3]
    # return 0


T = 10
for tc in range(1, T+1):
    N = int(input())

    tree = [[0] * 4 for _ in range(N+1)]
    for i in range(N):
        temp = input().split()
        if len(temp) == 4:
            tree[int(temp[0])][3] = temp[1]
            tree[int(temp[0])][0] = int(temp[2])
            tree[int(temp[0])][1] = int(temp[3])
            tree[int(temp[2])][2] = int(temp[0])
            tree[int(temp[3])][2] = int(temp[0])
        else:
            tree[int(temp[0])][3] = int(temp[1])

    print(f'#{tc} {postorder(1)}')