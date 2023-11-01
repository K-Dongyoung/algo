T = int(input())
for _ in range(1, T+1):
    C = int(input())
    count = [0] * 4
    if C >= 25:
        count[0] += C // 25
        C = C % 25
    if C >= 10:
        count[1] += C // 10
        C = C % 10
    if C >= 5:
        count[2] += C // 5
        C = C % 5
    if C >= 1:
        count[3] += C
    print(*count)
