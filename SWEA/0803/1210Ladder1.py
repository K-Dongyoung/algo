import sys; sys.stdin = open('ladder.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(100)]


    for i in range(len(L[99])):
        if L[99][i] == 2:
            col = i

    row = 99
    direction = ''

    while 0 <= row - 1 < 100:
        while L[row-1][col] == 1:
            if 0 <= col + 1 < 100 and 0 <= col - 1 < 100:
                if L[row][col + 1] == 0 and L[row][col - 1] == 0:
                    row -= 1
                if L[row][col + 1] == 1 or L[row][col - 1] == 1:
                    break
            if col - 1 < 0:
                if L[row][col + 1] == 0:
                    row -= 1
                if L[row][col + 1] == 1:
                    break
            if col + 1 >= 100:
                if L[row][col - 1] == 0:
                    row -= 1
                if L[row][col - 1] == 1:
                    break
            if row <= 0:
                break

        if 0 <= col + 1 < 100 and L[row][col+1] == 1 and L[row-1][col] == 1:
            col += 1
            direction = 'right'

        if 0 <= col - 1 < 100 and L[row][col-1] == 1 and L[row-1][col] == 1:
            col -= 1
            direction = 'left'

        while L[row-1][col] == 0:
            if direction == 'right':
                col += 1
            if direction == 'left':
                col -= 1

        row -= 1

        if row <= 0:
            break


    print(f'#{tc} {col}')

    # while True:
    #     if 0 <= col + 1 < 100 and 0 <= col - 1 < 100 and 0 <= row - 1 < 100:
    #         while L[row-1][col] == 1:
    #             row -= 1
    #             while L[row][col+1] == 1:
    #                 col += 1
    #                 # if col == 99:
    #                 #     row -= 1
    #             while L[row][col-1] == 1:
    #                 col -= 1
    #                 # if col == 0:
    #                 #     row -= 1
    #             if row == 0:
    #                 break
    #         if row == 0:
    #             break
    #     if row == 0:
    #         break