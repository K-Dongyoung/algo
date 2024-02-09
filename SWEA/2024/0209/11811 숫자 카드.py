"""
3
5
49679
5
08271
10
7797946543

"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = input()
    max_a = 0
    for n in a:
        if int(n) > max_a:
            max_a = int(n)
    L = [0] * (max_a + 1)
    for n in a:
        L[int(n)] += 1

    max_i = 0
    for i in range(len(L)):
        if int(L[i]) >= L[max_i]:
            max_i = i
    print(f"#{tc} {max_i} {L[max_i]}")