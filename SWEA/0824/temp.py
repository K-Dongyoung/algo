import sys
sys.stdin = open('code2.txt')

binary = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111',
}

code = {
    '211':0, '221':1, '122':2, '411':3, '132':4,
    '231':5, '114':6, '312':7, '213':8, '112':9,
}

def conversion():
    result = []
    s = set()
    for i in range(N):
        temp = []
        for j in range(M):
            temp.append(binary[arr[i][j]])
        s.add(''.join(temp).strip('0') + '0')
        s.discard('0')
    return list(s)

def cut(b):
    for string in b:
        stack = []
        count0 = 0
        count1 = 0
        for i in range(len(string)):
            if string[i] == '0':
                count0 += 1
                if count1 != 0:
                    stack.append(count1)
                    count1 = 0
            elif string[i] == '1':
                count1 += 1
                if count0 != 0:
                    stack.append(count0)
                    count0 = 0
            if len(stack) == 31:
                temp = []
                for i in range(len(stack)):
                    if i % 4 == 3:
                        continue
                    temp.append(stack[i])
                stack = []

    print(temp)





T = int(input())
for tc in range(1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    b = conversion()
    cut(b)