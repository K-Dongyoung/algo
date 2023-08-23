import sys
sys.stdin = open('simple_binary.txt')

def conversion(arr):
    result = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                temp = arr[i][j-55:j+1]
                break
    for i in range(0, 56, 7):
        result.append(code[temp[i: i+7]])
    return result

def decode(L):
    result = 0
    odd = 0
    even = 0
    for i in range(4):
        odd += L[i*2]
        even += L[i*2+1]
    result = odd * 3 + even
    if result%10:
        return 0
    return sum(L)

code = {
    '0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
    '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {decode(conversion(arr))}')