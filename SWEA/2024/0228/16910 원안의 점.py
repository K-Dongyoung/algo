import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = N
    for x in range(1, N):
        for y in range(1, N):
            if x**2 + y**2 <= N**2:
                count += 1

    count = count * 4 + 1
    print(f"#{tc} {count}")