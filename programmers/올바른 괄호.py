def solution(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if stack:
                stack.pop()
            else:
                return False

    # if len(stack) == 0:
    #     return True
    #
    # return False

    # 와 이거 좋네
    return len(stack) == 0
