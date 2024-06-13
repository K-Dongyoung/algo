N, B = map(int, input().split())
result = []
while N >= B:
    r = N % B
    if r > 9:
        result.append(chr(r - 10 + ord('A')))
    else:
        result.append(r)
    N //= B
if N > 9:
    result.append(chr(N - 10 + ord('A')))
else:
    result.append(N)
for i in range(len(result)):
    print(result.pop(), end='')