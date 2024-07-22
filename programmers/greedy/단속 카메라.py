"""
https://school.programmers.co.kr/learn/courses/30/lessons/42884
"""


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    temp = -30000
    for r in routes:
        if r[0] > temp:
            answer += 1
            temp = r[1]
    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
# return : 2
