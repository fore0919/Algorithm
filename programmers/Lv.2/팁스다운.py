"""
https://school.programmers.co.kr/learn/courses/30/lessons/12973
"""


def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    answer = 1 if not stack else 0
    return answer


s = "baabaa"  # result: 1
s = "cdcd"  # result: 0
