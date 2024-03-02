a = 1234
result = ''
divisor = 1

while a // (divisor * 10) > 0:
    divisor *= 10

while divisor >= 1:
    result += chr(a // divisor + 48)
    a %= divisor
    divisor //= 10

print(result + 'a')