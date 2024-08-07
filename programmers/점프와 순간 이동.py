# 다른 사람 코드 참고 해서 변경
def solution(n):
    ans = 0

    while n > 0:
        ans += n % 2
        n //= 2

    return ans


print(solution(5))
print(solution(6))
print(solution(5000))
