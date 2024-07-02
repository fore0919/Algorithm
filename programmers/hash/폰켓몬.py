"""
https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""


def solution(nums):
    answer = 0
    cnt = len(nums) // 2
    _set = len(set(nums))
    if _set <= cnt:
        answer = _set
    else:
        answer = cnt
    return answer


def solution2(nums2):
    return min(len(set(nums)), len(nums) / 2)


nums = [3, 1, 2, 3]  # answer = 2
nums2 = [3, 3, 3, 2, 2, 4]  # answer = 3
nums3 = [3, 3, 3, 2, 2, 2]  # answer = 2
