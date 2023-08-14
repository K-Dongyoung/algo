import sys
sys.stdin = open('trainfly.txt')

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    ans = ((D * F) / (A+B))
    print(f'#{tc} {ans}')