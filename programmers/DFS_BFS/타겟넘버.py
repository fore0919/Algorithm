"""
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""


# DFS - recursion
def solution(numbers, target):
    answer = 0
    length = len(numbers)

    def dfs(index, number):
        if length == index:
            if number == target:
                nonlocal answer
                answer += 1
                return
        else:
            dfs(index + 1, number + numbers[index])
            dfs(index + 1, number - numbers[index])

    dfs(0, 0)
    return answer


# DFS - stack
def solution2(numbers, target):
    answer = 0
    n = len(numbers)
    _list = [[numbers[0], 0], [-1 * numbers[0], 0]]
    while _list:
        temp, idx = _list.pop()
        idx += 1
        if idx < n:
            _list.append([temp + numbers[idx], idx])
            _list.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


# BFS - queue
def solution3(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        temp = []
        for parent in leaves:
            temp.append(parent + num)
            temp.append(parent - num)
        leaves = temp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
# 	return :5

numbers = [4, 1, 2, 1]
target = 4
# return : 2

print(solution(numbers, target))
print(solution2(numbers, target))
print(solution3(numbers, target))
