a = 1234
result = []
while a > 0:
    result.append(chr(a % 10 + 48))
    a //= 10

L = len(result)
for i in range(L // 2):
    result[i], result[L - i - 1] = result[L - i - 1], result[i]

result = "".join(result)
print(result + 'a')

"""
a = 1234
temp = []
while a > 0:
    temp.append(chr(a % 10 + 48))
    a //= 10

result = ''
for c in temp[::-1]:
    result += c

print(result)
"""