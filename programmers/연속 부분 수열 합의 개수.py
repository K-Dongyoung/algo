def solution(elements):
    length_elements = len(elements)
    a = elements + elements[:length_elements - 1]
    s = set()
    for i in range(length_elements):
        for j in range(1, length_elements):
            s.add(sum(a[i:i + j]))
    return len(s) + 1


def solution2(elements):
    length_elements = len(elements)
    a = elements + elements[:length_elements - 1]
    s = set()
    for i in range(length_elements):
        b = 0
        for j in range(length_elements - 1):
            b += a[i + j]
            s.add(b)
    return len(s) + 1


def solution3(elements):
    length_elements = len(elements)
    s = set()
    for i in range(length_elements):
        b = 0
        for j in range(length_elements - 1):
            b += elements[(i + j) % length_elements]
            s.add(b)
    return len(s) + 1


print(solution3([7, 9, 1, 1, 4]))
