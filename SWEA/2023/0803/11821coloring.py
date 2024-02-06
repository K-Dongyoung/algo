T = int(input())
for tc in range(1, T+1):
    N = int(input())

    set_r = set()
    set_b = set()

    for _ in range(N):
        row1, col1, row2, col2, rb = map(int, input().split())
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                if rb == 1:
                    set_r.add((row, col))
                if rb == 2:
                    set_b.add((row, col))

    set_inter = set_r & set_b
    print(f'#{tc} {len(set_inter)}')