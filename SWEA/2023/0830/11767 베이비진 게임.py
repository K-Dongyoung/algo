import sys
sys.stdin = open('baby gin game.txt')

def f():
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(len(arr)):
        if i % 2 == 0:
            player1[arr[i]] += 1
            if player1[arr[i]] == 3:
                return 1
            elif player1[arr[i]] == 1:
                idx = arr[i]
                if idx-2 >= 0 and player1[idx-2] >= 1 and player1[idx-1] >= 1:
                    return 1
                elif idx-1 >= 0 and idx+1 <= 6 and player1[idx-1] >= 1 and player1[idx+1] >= 1:
                    return 1
                elif idx+2 <= 9 and player1[idx+1] >= 1 and player1[idx+2] >= 1:
                    return 1
        else:
            player2[arr[i]] += 1
            if player2[arr[i]] == 3:
                return 2
            elif player2[arr[i]] == 1:
                idx = arr[i]
                if idx-2 >= 0 and player2[idx-2] >= 1 and player2[idx-1] >= 1:
                    return 2
                elif idx-1 >= 0 and idx+1 <= 6 and player2[idx-1] >= 1 and player2[idx+1] >= 1:
                    return 2
                elif idx+2 <= 9 and player2[idx+1] >= 1 and player2[idx+2] >= 1:
                    return 2
    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {f()}')