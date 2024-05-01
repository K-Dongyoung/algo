def solution(A, B):
    answer = 0
    A.sort(reverse=True) # 내림차순 정렬
    B.sort(reverse=True)
    i = 0 # A 참조할 인덱스
    a_len = len(A)

    for b in B:
        while i < a_len:
            if b > A[i]: # b가 더 커서 이기는 경우
                answer += 1
                i += 1
                break
            i += 1 # b가 작을 경우 A[i]보다 작은 값이랑 재대결 한다고 가정

    return answer


A = [5, 1, 3, 7]
B = [2, 2, 6, 8]
print(solution(A, B))