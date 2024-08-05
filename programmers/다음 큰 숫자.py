def solution(n):
    cnt_1 = bin(n)[2:].count("1")
    while True:
        n += 1
        if cnt_1 == bin(n)[2:].count("1"):
            return n

print(solution(78))
print(solution(15))
print(solution(14))
