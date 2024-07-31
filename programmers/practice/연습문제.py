"""
https://school.programmers.co.kr/learn/courses/30/lessons/12941
"""


def solution(A, B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))


A = [1, 4, 2]
B = [5, 4, 4]
# answer: 29
A = [1, 2]
B = [3, 4]
# answer: 10

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12924
"""


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        _sum = 0
        for j in range(i, n + 1):
            _sum += j
            if _sum == n:
                answer += 1
                break
            elif _sum > n:
                break
    return answer


n = 15
# result: 4

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12911
"""


def solution(n):
    answer = 0
    cnt = bin(n)[2:].count("1")
    while True:
        n += 1
        if cnt == bin(n)[2:].count("1"):
            answer = n
            break
    return answer


n = 78  # result: 83
n = 15  # result: 23

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12945
"""


def solution(n):
    answer = [0, 1]
    for i in range(2, n + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)
    return answer[-1]


n = 3
# return: 2
n = 5
# return: 5

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12914
"""


def solution(n):
    answer = 0
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    answer = b % 1234567
    return answer


n = 4
# result : 5
n = 3
# result: 3

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12953
"""


def solution(arr):
    answer = 0

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    a = arr.pop(0)
    while len(arr) > 0:
        b = arr.pop(0)
        a = a * b / gcd(a, b)

    answer = a
    return answer


arr = [2, 6, 8, 14]
# result: 168
arr = [1, 2, 3]
# result: 6
