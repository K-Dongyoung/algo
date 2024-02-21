import sys

sys.stdin = open("sample_input.txt")


def find_number_of_times(P, target):
    start = 1
    end = P
    count = 0
    while start <= end:
        middle = int((start + end) / 2)
        count += 1
        if middle == target:
            return count
        elif middle > target:
            end = middle
        else:
            start = middle


T = int(input())
for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    if find_number_of_times(P, Pa) < find_number_of_times(P, Pb):
        answer = "A"
    elif find_number_of_times(P, Pa) > find_number_of_times(P, Pb):
        answer = "B"
    else:
        answer = "0"
    print(f"#{tc} {answer}")
