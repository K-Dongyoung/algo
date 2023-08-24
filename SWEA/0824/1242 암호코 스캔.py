import sys
sys.stdin = open('code.txt')

binary = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111',
}

code = {
    '221':0, '221':1, '122':2, '411':3, '132':4,
    '231':5, '114':6, '312':7, '213':8, '112':9,
}

def get(L):
    result = []
    temp = set()
    for i in range(N):
        temp.add(L[i])
    temp.remove(L[0])
    for i in range(len(temp)):
        result.append(temp.pop())
    return result

def convert(L):
    result = []
    for string in L:
        temp = []
        for c in string:
            temp.append(binary[c])
        result.append(''.join(temp))
    return result

def find_magnification(string):
    pass

def division():
    pass

def decode(string):
    pass


T = int(input())
for tc in range(1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    hexa = get(arr)
    b = convert(hexa)

    print(b)
