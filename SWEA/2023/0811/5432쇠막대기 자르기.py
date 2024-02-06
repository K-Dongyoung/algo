import sys
sys.stdin = open('ironbar.txt')

T = int(input())
for tc in range(1, T+1):
    temp = input()
    p = temp.replace('()', 'R')
    total_count = 0
    current_ironbar = 0
    for c in p:
        if c == '(':
            total_count += 1
            current_ironbar += 1
        if c == 'R':
            total_count += current_ironbar
        if c == ')':
            current_ironbar -= 1

    print(f'#{tc} {total_count}')