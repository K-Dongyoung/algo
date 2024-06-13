N = int(input())
count = 0
for _ in range(N):
    word = input()
    cnt_alphabet = [2] * (ord('z')-ord('a')+1)
    for i in range(len(word)):
        if i-1 >= 0 and word[i-1] == word[i]:
            continue
        cnt_alphabet[ord(word[i])-ord('a')] -= 1

    flag =True
    for n in cnt_alphabet:
        if n < 1:
            flag = False
            break
    if flag:
        count += 1

print(count)