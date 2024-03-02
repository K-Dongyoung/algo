a = '1234'
result = 0

for c in a:
    result = result * 10 + ord(c) - ord('0')

print(result + 1)