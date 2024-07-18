"""
https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""


def solution(people, limit):
    answer = 0
    people.sort()

    start_idx = 0
    end_idx = len(people) - 1

    while start_idx < end_idx:
        if people[start_idx] + people[end_idx] <= limit:
            start_idx += 1
            answer += 1
        end_idx -= 1
    answer = len(people) - answer
    return answer


people = [70, 50, 80, 50]
limit = 100
# return : 3
people = [70, 80, 50]
limit = 100
# return: 3
