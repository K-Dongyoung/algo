import sys
sys.stdin = open('sudoku.txt')

def sudoku(N):

    for i in range(N):
        row = set()
        col = set()
        for j in range(N):
            row.add(puzzle[i][j])
            col.add(puzzle[j][i])
        if len(row) < N or len(col) < N:
            return 0

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            temp = set()
            for k in range(3):
                for m in range(3):
                    temp.add(puzzle[k+i][m+j])
            if len(temp) < N:
                return 0

    return 1


T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {sudoku(9)}')