def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0 and s[i].isalpha():
            answer += s[i].capitalize()
        elif s[i - 1] == " " and s[i].isalpha():
            answer += s[i].capitalize()
        else:
            answer += s[i].lower()
    return answer


print(solution("3people unFollowed me"))
print(solution("for the last week"))
