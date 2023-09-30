string = input()
z = ord('z')-ord('a') + 1
arr = [0] * z
for c in string:
    if 0 <= ord(c) - ord('A') < z:
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