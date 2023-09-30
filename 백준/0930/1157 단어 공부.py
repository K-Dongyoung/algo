string = input()
arr = [0] * 26
for c in string:
    if c.isupper():
        arr[ord(c) - ord('A')] += 1
    else:
        arr[ord(c) - ord('a')] += 1
cnt = 0
idx = -1
for i in range(len(arr)):
    if arr[i] == max(arr):
        cnt += 1
        idx = i
if cnt == 1:
    print(chr(idx+ord('A')))
else:
    print('?')