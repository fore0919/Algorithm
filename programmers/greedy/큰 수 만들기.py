"""
https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""

from itertools import combinations


# 시간 초과 실패
def failed_solution(number, k):
    answer = ""
    temp = list(combinations(number, len(number) - k))
    temp.sort()
    answer += "".join(temp)
    return answer


def solution(number, k):
    answer = ""
    stack = []
    for n in number:
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    if k != 0:
        stack = stack[:-k]
    answer = "".join(stack)
    return answer


number = "1924"
k = 2  # return : "94"
number = "1231234"
k = 3  # return : "3234"
number = "4177252841"
k = 4  # return :"775841"

print(solution(number, k))
