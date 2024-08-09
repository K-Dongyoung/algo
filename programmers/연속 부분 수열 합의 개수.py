def solution(elements):
    length_elements = len(elements)
    a = elements + elements[:length_elements - 1]
    s = set()
    for i in range(length_elements):
        for j in range(1, length_elements):
            s.add(sum(a[i:i + j]))
    return len(s) + 1


print(solution([7, 9, 1, 1, 4]))
