import sys
sys.stdin = open('perfect.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    L = len(cards)
    print(f'#{tc}', end=' ')
    for i in range(L // 2):
        print(cards[i], end=' ')
        print(cards[i + (L + L % 2) // 2], end=' ')
    if L % 2:
        print(cards[L // 2], end=' ')
    print()