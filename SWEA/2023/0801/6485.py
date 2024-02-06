T = int(input())
for tc in range(1, T+1):

    N = int(input())

    count = []
    count = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            count[i] += 1

    P = int(input())

    temp = []

    for _ in range(1, P+1):
        C = int(input())
        temp.append(count[C])

    print(f'#{tc}', *temp)