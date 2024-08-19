"""
https://school.programmers.co.kr/learn/courses/30/lessons/70129
"""


def solution(s):
    rnd, cnt = 0, 0
    while s != "1":
        rnd += 1
        length = s.count("1")
        cnt += len(s) - length
        s = bin(length)[2:]
    return [rnd, cnt]


s = "110010101001"
# result = [3,8]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/76502
"""


def solution(s):
    answer = 0
    x = 0
    s = list(s)
    dic = {"}": "{", "]": "[", ")": "("}
    while len(s) != x:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == dic.get(s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        if not stack:
            answer += 1
        s.append(s.pop(0))
        x += 1
    return answer


s = "[](){}"
# result :3

"""
https://school.programmers.co.kr/learn/courses/30/lessons/87390
"""


def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer


n = 3
left = 2
right = 5  # result: [3,2,2,3]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/77885
"""


def solution(numbers):
    answer = []
    for number in numbers:
        binary = list("0" + bin(number)[2:])
        idx = "".join(binary).rfind("0")
        binary[idx] = "1"
        if number % 2 == 1:
            binary[idx + 1] = "0"
        answer.append(int("".join(binary), 2))
    return answer


numbers = [2, 7]
# result : [3,11]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/68936
"""


def solution(arr):
    answer = [0, 0]
    length = len(arr)

    def recursion(x, y, length):
        current = arr[x][y]
        for i in range(x, x + length):
            for j in range(y, y + length):
                if arr[i][j] != current:
                    length //= 2
                    recursion(x, y, length)
                    recursion(x + length, y, length)
                    recursion(x, y + length, length)
                    recursion(x + length, y + length, length)
                    return
        answer[current] += 1

    recursion(0, 0, length)
    return answer


arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
# result: [4,9]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/68645
"""


def solution(n):
    answer = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    return sum(answer, [])
