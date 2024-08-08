"""
https://school.programmers.co.kr/learn/courses/30/lessons/12981
"""


def solution(n, words):
    word = []
    for i in range(1, len(words)):
        word.append(words[i - 1])
        string = word[-1][-1]
        if not words[i].startswith(string) or words[i] in word:
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0]


n = 3
words = [
    "tank",
    "kick",
    "know",
    "wheel",
    "land",
    "dream",
    "mother",
    "robot",
    "tank",
]
# result : [3,3]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/49993
"""


def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        skills = list(st)
        cnt = 0
        idx = 0
        while len(st) > cnt:
            current = skills[0]
            if idx >= len(skill) or current not in skill:
                skills.pop(0)
            elif current == skill[idx]:
                skills.pop(0)
                idx += 1
            cnt += 1
        if not skills:
            answer += 1
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# result = 2
