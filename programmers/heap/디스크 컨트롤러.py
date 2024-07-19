"""
https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""

import heapq


def solution(jobs):
    answer = 0
    now = 0
    cnt = 0
    start = -1
    heap = []

    while cnt < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            cnt += 1
        else:
            now += 1

    return answer // len(jobs)


jobs = [[0, 3], [1, 9], [2, 6]]
# return : 9

print(solution(jobs))
