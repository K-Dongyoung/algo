import sys
sys.stdin = open("GNS_test_input.txt")


T = int(input())
for tc in range(1, T + 1):
    _, length = input().split()
    arr = input().split()

    d = {
        "ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0,
        "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0
    }

    for num in arr:
        d[num] += 1

    print(f"#{tc}")
    for k, v in d.items():
        print((k + " ") * v, end="")
    print()
