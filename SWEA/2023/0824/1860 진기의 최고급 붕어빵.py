import sys
sys.stdin = open('boong.txt')

def customer():
    for second in seconds:
        counting[second] += -1

def boong(M, K):
    for i in range(M, len(counting), M):
        counting[i] += K

def waiting():
    sum = 0
    for i in range(len(counting)):
        sum += counting[i]
        if sum < 0:
            return 'Impossible'
    return 'Possible'


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    seconds = list(map(int, input().split()))
    counting = [0] * (max(seconds) + 1)
    customer()
    boong(M, K)
    print(f'#{tc} {waiting()}')