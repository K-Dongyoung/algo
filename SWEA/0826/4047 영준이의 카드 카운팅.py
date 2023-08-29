import sys
sys.stdin = open('card.txt')

def f():
    idx = 0
    need = 0
    while idx < len(card) - 2:
        if card[idx] == 'S':
            tmp = (ord(card[idx+1])-ord('0')) * 10 + ord(card[idx+2])-ord('0')
            S[tmp] -= 1
            if S[tmp] < 0:
                return 'ERROR'
        elif card[idx] == 'D':
            tmp = (ord(card[idx + 1]) - ord('0')) * 10 + ord(card[idx + 2]) - ord('0')
            D[tmp] -= 1
            if D[tmp] < 0:
                return 'ERROR'
        elif card[idx] == 'H':
            tmp = (ord(card[idx + 1]) - ord('0')) * 10 + ord(card[idx + 2]) - ord('0')
            H[tmp] -= 1
            if H[tmp] < 0:
                return 'ERROR'
        elif card[idx] == 'C':
            tmp = (ord(card[idx + 1]) - ord('0')) * 10 + ord(card[idx + 2]) - ord('0')
            C[tmp] -= 1
            if C[tmp] < 0:
                return 'ERROR'
        idx += 3
    return sum(S), sum(D), sum(H), sum(C)

T = int(input())
for tc in range(1, T+1):
    card = input()
    S = [0]+[1] * 13
    D = [0]+[1] * 13
    H = [0]+[1] * 13
    C = [0]+[1] * 13

    temp = f()
    if temp == 'ERROR':
        print(f'#{tc} {temp}')
    else:
        print(f'#{tc}', *temp)
    # 부족한 카드 수 S D H C 순으로 출력, 이미 겹치는 카드가 있으면 ERROR 출력