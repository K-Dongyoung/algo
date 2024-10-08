def solution(people, limit):
    ans = 0
    people.sort()
    s = 0
    e = len(people) - 1
    while s <= e:
        if people[s] + people[e] <= limit:
            s += 1
        ans += 1
        e -= 1
    return ans


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))