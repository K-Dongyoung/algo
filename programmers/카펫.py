def solution(brown, yellow):
    a = (brown - 4) // 2
    for i in range(1, a // 2 + 1):
        b = i
        c = a - i
        if b * c == yellow:
            return [c + 2, b + 2]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
