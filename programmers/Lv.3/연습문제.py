"""
https://school.programmers.co.kr/learn/courses/30/lessons/12927
"""


# 효율성 통과 실패
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer
    while n:
        works[works.index(max(works))] -= 1
        n -= 1
    return sum([work * work for work in works])


# 효율성 통과 성공
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0

    works.sort(reverse=True)
    for i in range(n):
        m = max(works)
        j = 0
        while 1:
            if works[j] != m:
                break
            works[j] -= 1
            n -= 1
            j += 1
            if n == 0:
                break
        if n == 0:
            break
    for work in works:
        answer += work * work
    return answer


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12938#
"""
import math


def solution(n, s):
    answer = []
    cnt = s % n
    if s < n:
        return [-1]
    while len(answer) != n:
        if cnt > 0:
            cnt -= 1
            answer.append(math.ceil(s / n))
        else:
            answer.append(s // n)
    return sorted(answer)


"""
https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3
"""

from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [-1] * (n + 1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque([1])
    distance[1] = 0

    while q:
        current = q.popleft()
        for i in graph[current]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[current] + 1

    return distance.count(max(distance))


"""
https://school.programmers.co.kr/learn/courses/30/lessons/43164
"""

from collections import deque


### BFS
def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))
    q = deque([(["ICN"], tickets)])
    while q:
        path, ticket = q.popleft()
        if not len(ticket):
            answer = path
            break
        idx = -1
        for i in range(len(ticket)):
            if ticket[i][0] == path[-1]:
                idx = i
                break
        if idx != -1:
            while idx < len(ticket) and ticket[idx][0] == path[-1]:
                q.append(
                    (path + [ticket[idx][1]], ticket[:idx] + ticket[idx + 1 :])
                )
                idx += 1
    return answer


from collections import defaultdict


### DFS - stack
def solution(tickets):
    answer = []
    stack = defaultdict(list)
    path = ["ICN"]
    for k, v in tickets:
        stack[k].append(v)
    for key in stack.keys():
        stack[key].sort(reverse=True)

    while path:
        current = path[-1]
        if current not in stack or len(stack[current]) == 0:
            answer.append(path.pop())
        else:
            path.append(stack[current].pop())
    return answer[::-1]


### DFS - recursion
def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))

    def recursion(ticket, path):
        if len(ticket) == 0:
            return path
        current = path[-1]
        idx = -1

        for i in range(len(ticket)):
            if ticket[i][0] == current:
                idx = i
                break
        if idx == -1:
            return []

        while ticket[idx][0] == current:
            answer = recursion(
                ticket[:idx] + ticket[idx + 1 :], path + [ticket[idx][1]]
            )
            if answer != []:
                return answer
            idx += 1
        return answer

    return recursion(tickets, ["ICN"])


"""
https://school.programmers.co.kr/learn/courses/30/lessons/161988
"""


def solution(sequence):
    answer = [[0 for _ in range(len(sequence) + 1)] for _ in range(2)]
    temp = 1
    for i in range(len(sequence)):
        answer[0][i + 1] = answer[0][i] - sequence[i] * temp
        answer[1][i + 1] = answer[1][i] + sequence[i] * temp
        temp *= -1
    return max(max(answer[0]) - min(answer[0]), max(answer[1]) - min(answer[1]))


"""
https://school.programmers.co.kr/learn/courses/30/lessons/49191
"""


def solution(n, results):
    answer = 0
    win = [set() for _ in range(n + 1)]
    lose = [set() for _ in range(n + 1)]
    for x, y in results:
        win[x].add(y)
        lose[y].add(x)
    for i in range(1, n + 1):
        for j in win[i]:
            lose[j].update(lose[i])
        for j in lose[i]:
            win[j].update(win[i])
    for player in range(1, n + 1):
        count = len(win[player]) + len(lose[player])
        if count == n - 1:
            answer += 1
    return answer
