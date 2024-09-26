from collections import deque


# def solution(priorities, location):
#     priorities = deque(priorities)
#     cnt = 0
#     while priorities:
#         M = max(priorities)
#         if location > 0:
#             if priorities[0] < M:
#                 x = priorities.popleft()
#                 priorities.append(x)
#                 location -= 1
#             elif priorities[0] == M:
#                 priorities.popleft()
#                 cnt += 1
#                 location -= 1
#
#         elif location == 0:
#             if priorities[0] < M:
#                 x = priorities.popleft()
#                 priorities.append(x)
#                 location += len(priorities) - 1
#             elif priorities[0] == M:
#                 return cnt + 1

def solution(priorities, location):
    priorities = deque(priorities)
    cnt = 0
    M = max(priorities)
    while priorities:
        if priorities[0] < M:
            x = priorities.popleft()
            priorities.append(x)
            if location == 0:
                location += len(priorities)
            location -= 1


        elif priorities[0] == M:
            priorities.popleft()
            cnt += 1
            if location == 0:
                return cnt
            location -= 1
            M = max(priorities)


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
