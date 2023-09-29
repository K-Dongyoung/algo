string = list(input())
L = len(string)
flag = True
for i in range(L//2):
    if string[i] != string[L-i-1]:
        flag = False
if flag:
    print(1)
else:
    print(0)