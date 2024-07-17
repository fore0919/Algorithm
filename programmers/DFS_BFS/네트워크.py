"""
https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""

from collections import deque


def solution(n, computers):
    answer = 0

    def dfs(i):
        visit[i] = 1
        for j in range(n):
            if computers[i][j] and not visit[j]:
                dfs(j)

    def bfs(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visit[i] = 1
            for j in range(n):
                if computers[i][j] and not visit[j]:
                    q.append(j)

    visit = [0 for i in range(len(computers))]
    for i in range(n):
        if not visit[i]:
            dfs(i)
            # bfs(i)
            answer += 1
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# result : 2
n2 = 3
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# result : 1

print(solution(n, computers2))
