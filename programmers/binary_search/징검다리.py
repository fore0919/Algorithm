"""
https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""


def solution(distance, rocks, n):
    left = 1
    right = distance
    rocks.append(distance)
    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        cnt, visit = 0, 0
        for r in rocks:
            rock = r - visit
            if rock < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                visit = r
        if cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer
