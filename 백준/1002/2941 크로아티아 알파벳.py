S = input()
N = len(S)
cnt = 0
for i in range(N):
    if S[i] not in '=-':
        cnt += 1
    if S[i] == 'd':
        if i+2 < N and S[i+1] == 'z' and S[i+2] == '=':
            cnt -= 1
    elif S[i] in 'ln':
        if i+1 < N and S[i+1] == 'j':
            cnt -= 1
print(cnt)
