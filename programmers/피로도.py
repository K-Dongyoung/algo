def solution(k, dungeons):
    answer = []
    used = [0 for _ in range(len(dungeons))]

    def p(chosen):
        if len(chosen) == len(dungeons):
            answer.append(return_finished_dungeons(chosen))
            return

        for i in range(len(dungeons)):
            if not used[i]:
                chosen.append(dungeons[i])
                used[i] = 1
                p(chosen)
                used[i] = 0
                chosen.pop()

    def return_finished_dungeons(l):
        r = k
        cnt = 0
        for d in l:
            if r < d[0]:
                break
            r -= d[1]
            cnt += 1
        return cnt

    p([])
    return max(answer)


print(solution(80, [[80,20],[50,40],[30,10]]))