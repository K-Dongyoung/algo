T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            count[j] += 1
    P = int(input())
    print(f"#{tc}", end=" ")
    for i in range(P):
        C = int(input())
        print(f"{count[C]}", end=" ")
    print()