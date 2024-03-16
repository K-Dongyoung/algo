import sys
sys.stdin = open("input.txt")

def isPalindrome(table, length):
    for row in range(100):
        for col in range(100 - length + 1):
            for i in range(length // 2):
                if table[row][col + i] != table[row][col + length - 1 - i]:
                    break
                if i == length // 2 - 1:
                    return True

for _ in range(10):
    tc = input()
    table = [input() for _ in range(100)]
    table_t = list(zip(*table))
    max_length = 1

    for i in range(100, 1, -1):
        if isPalindrome(table, i):
            max_length = i
            break
        if isPalindrome(table_t, i):
            max_length = i
            break

    print(f"#{tc} {max_length}")