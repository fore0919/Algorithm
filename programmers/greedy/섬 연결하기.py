"""
https://school.programmers.co.kr/learn/courses/30/lessons/42861
"""


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    connect = set([costs[0][0]])
    while len(connect) != n:
        for c in costs:
            if c[0] in connect and c[1] in connect:
                continue
            if c[0] in connect or c[1] in connect:
                connect.update([c[0], c[1]])
                answer += c[2]
                break
    return answer


n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
# return : 4

print(solution(n, costs))
