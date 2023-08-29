import sys
sys.stdin = open('card.txt')

def f():
    need = [13, 13, 13, 13]
    for i in range(0, len(card), 3):
        num = int(card[i+1] + card[i+2])
        have[d[card[i]]][num] += 1
        if have[d[card[i]]][num] > 1:
            return ['ERROR']
        need[d[card[i]]] -= 1
    return need

T = int(input())
for tc in range(1, T+1):
    card = input()
    have = [[0]*14 for _ in range(4)]
    d = {'S':0, 'D':1, 'H':2, 'C':3}

    print(f'#{tc}', *f())

    # 부족한 카드 수 S D H C 순으로 출력, 이미 겹치는 카드가 있으면 ERROR 출력