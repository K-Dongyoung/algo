def solution(n, words):
    i = find_index(words)
    if i == -1:
        return [0, 0]
    else:
        return [i % n + 1, i // n + 1]


def find_index(words):
    s = set()
    for i in range(len(words)):
        if words[i] not in s:
            s.add(words[i])
        else:
            return i
        if i > 0 and words[i][0] != words[i - 1][-1]:
            return i
    return -1

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure",
                   "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
