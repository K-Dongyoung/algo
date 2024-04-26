def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    a_len = len(A)

    for b in B:
        while i < a_len:
            if b > A[i]:
                answer += 1
                i += 1
                break
            i += 1

    return answer


A = [5, 1, 3, 7]
B = [2, 2, 6, 8]
print(solution(A, B))
