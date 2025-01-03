"""
https://school.programmers.co.kr/learn/courses/30/lessons/64064
"""


def solution(user_id, banned_id):
    answer = []
    result = [[]]
    for banned in banned_id:
        idx = []
        _list = []
        for i, j in enumerate(banned):
            if j == "*":
                idx.append(i)

        for user in user_id:
            user_name = list(user)
            if len(user) == len(banned):
                for k in idx:
                    user_name[k] = "*"

            user_name = "".join(user_name)
            if user_name == banned:
                for r in result:
                    if user not in r:
                        _list.append(r + [user])
        result = _list

    for name in result:
        if set(name) not in answer:
            answer.append(set(name))

    return len(answer)


"""
https://school.programmers.co.kr/learn/courses/30/lessons/67258
"""

from collections import defaultdict


def solution(gems):
    min_gems = int(1e9)
    len_gems = len(gems)
    n_gems = len(set(gems))
    end = 0
    temp = defaultdict(lambda: 0)
    for start, gem in enumerate(gems):
        while len(temp) < n_gems and end < len_gems:
            temp[gems[end]] += 1
            end += 1
        if len(temp) == n_gems:
            if min_gems > end - start:
                min_gems = end - start
                result = [start + 1, end]
        temp[gem] -= 1
        if temp[gem] == 0:
            del temp[gem]
    return result


"""
https://school.programmers.co.kr/learn/courses/30/lessons/64062
"""


# 효율성 통과 X
def solution(stones, k):
    windows = max(stones[:k])
    for i in range(k, len(stones) - k + 1):
        num = max(stones[i : k + i])
        windows = min(windows, num)
    return windows


# 효율성 통과 O
from collections import deque


def solution(stones, k):
    stones = list(zip(range(1, len(stones) + 1), stones))
    q = deque()
    answer = float("inf")
    for idx, val in stones:
        while q:
            if q[0][0] <= (idx - k):
                q.popleft()
            elif q[-1][1] < val:
                q.pop()
            else:
                break
        q.append((idx, val))
        if idx >= k:
            answer = min(q[0][1], answer)
    return answer


"""
https://school.programmers.co.kr/learn/courses/30/lessons/17678
"""

from collections import deque
from datetime import datetime, timedelta


def solution(n, t, m, timetable):
    answer = []
    start = datetime.strptime("09:00", "%H:%M")
    timetable.sort()
    q = deque(timetable)

    for i in range(1, n + 1):
        answer.append(start)
        start += timedelta(minutes=t)

    for j in range(1, len(answer) + 1):
        cnt = m
        if (len(q) - q.count("23:59")) < cnt:
            return answer[-1].strftime("%H:%M")

        if j == n and cnt < len(q):
            time = datetime.strptime(q[cnt - 1], "%H:%M")
            break

        while q:
            time = datetime.strptime(q[0], "%H:%M")
            if time <= answer[j - 1] and cnt > 0:
                q.popleft()
                cnt -= 1
            else:
                break

    return (time - timedelta(minutes=1)).strftime("%H:%M")


"""
https://school.programmers.co.kr/learn/courses/30/lessons/67259?language=python3
"""

import heapq
from sys import maxsize


def solution(board):
    n = len(board)
    cost = [[[maxsize] * 4 for _ in range(n)] for _ in range(n)]
    visited = [[[False] * 4 for _ in range(n)] for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heap = []
    for i in range(4):
        heapq.heappush(heap, (0, 0, 0, i))
        cost[0][0][i] = 0
    while heap:
        current_cost, y, x, di = heapq.heappop(heap)
        if visited[y][x][di]:
            continue
        visited[y][x][di] = True
        for i, (dy, dx) in enumerate(directions):
            ny, nx = dy + y, dx + x
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                new_cost = current_cost + (100 if i == di else 600)
                if new_cost < cost[ny][nx][i]:
                    cost[ny][nx][i] = new_cost
                heapq.heappush(heap, (new_cost, ny, nx, i))
    return min(cost[n - 1][n - 1])


"""
https://school.programmers.co.kr/learn/courses/30/lessons/60059
"""


def solution(key, lock):
    def check(x, y, key):
        for i in range(m):
            for j in range(m):
                if 0 <= x + i < n and 0 <= y + j < n:
                    if lock[x + i][y + j] + key[i][j] != 1:
                        return False
        for i in range(n):
            for j in range(n):
                if lock[i][j] == 0:
                    if not (
                        0 <= i - x < m
                        and 0 <= j - y < m
                        and key[i - x][j - y] == 1
                    ):
                        return False
        return True

    cnt = 4
    m, n = len(key), len(lock)
    while cnt > 0:
        rotation = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(len(key)):
            for j in range(len(key[i])):
                rotation[j][-(1 + i)] = key[i][j]
        cnt -= 1
        key = rotation
        for x in range(-m + 1, n):
            for y in range(-m + 1, n):
                if check(x, y, key):
                    return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
