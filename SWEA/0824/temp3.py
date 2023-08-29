import sys
sys.stdin = open('code.txt')

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

def decode(string):
    stack = []
    count0 = 0
    count1 = 0
    for i in range(len(string)-1,-1,-1):
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
    temp = stack[1:]

    temp2 = []
    for i in range(len(temp)):
        if i%4 == 3:
            continue
        temp2.append(temp[i])
    temp2.reverse()

    temp4 = []
    for i in range(len(temp2)//3):
        temp3 = []
        temp3.append(temp2[i*3])
        temp3.append(temp2[i*3+1])
        temp3.append(temp2[i*3+2])
        temp3 = list(map(str, map(lambda x:x//min(temp3), temp3)))
        temp4.append(''.join(temp3))

    sum = 0
    for i in range(len(temp4)//8):
        odd = code[temp4[i * 8]] + code[temp4[i * 8 + 2]] + code[temp4[i * 8 + 4]] + code[temp4[i * 8 + 6]]
        even = code[temp4[i * 8 + 1]] + code[temp4[i * 8 + 3]] + code[temp4[i * 8 + 5]] + code[temp4[i * 8 + 7]]
        if (odd * 3 + even) % 10 == 0:
            sum += odd + even
    return sum


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    hexa = get(arr)
    b = convert(hexa)

    sum = 0
    for i in b:
        sum += decode(i)
    print(f'#{tc} {sum}')