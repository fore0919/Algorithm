"""
https://school.programmers.co.kr/learn/courses/30/lessons/70129
"""


def solution(s):
    rnd, cnt = 0, 0
    while s != "1":
        rnd += 1
        length = s.count("1")
        cnt += len(s) - length
        s = bin(length)[2:]
    return [rnd, cnt]


s = "110010101001"
# result = [3,8]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/76502
"""


def solution(s):
    answer = 0
    x = 0
    s = list(s)
    dic = {"}": "{", "]": "[", ")": "("}
    while len(s) != x:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == dic.get(s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        if not stack:
            answer += 1
        s.append(s.pop(0))
        x += 1
    return answer


s = "[](){}"
# result :3
