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

"""
https://school.programmers.co.kr/learn/courses/30/lessons/138476
"""

from collections import Counter


def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    sort = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    for i, j in sort:
        k -= j
        answer += 1
        if k <= 0:
            break
    return answer


k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]


"""
https://school.programmers.co.kr/learn/courses/30/lessons/131701
"""


def solution(elements):
    answer = set()
    length = len(elements)
    elements = elements * 2

    for i in range(length):
        for j in range(length):
            answer.add(sum(elements[j : j + i + 1]))
    return len(answer)


elements = [7, 9, 1, 1, 4]
# result : 18


"""
https://school.programmers.co.kr/learn/courses/30/lessons/131127
"""


def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        temp = discount[i : i + 10]
        cnt = []
        for j in range(len(want)):
            if temp.count(want[j]) >= number[j]:
                cnt.append(True)
        if len(cnt) == len(want):
            answer += 1
    return answer


from collections import Counter


def solution2(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n

    for i in range(len(discount) - 9):
        c = Counter(discount[i : i + 10])
        print(c)
        if c == check:
            answer += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = [
    "chicken",
    "apple",
    "apple",
    "banana",
    "rice",
    "apple",
    "pork",
    "banana",
    "pork",
    "rice",
    "pot",
    "banana",
    "apple",
    "banana",
]
# result : 3

"""
https://school.programmers.co.kr/learn/courses/30/lessons/154539
"""


def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer


numbers = [2, 3, 3, 5]
# result: [3, 5, 5, -1]
numbers = [9, 1, 5, 3, 6, 2]
# result: [-1, 5, 6, 6, -1, -1]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""


def solution(topping):
    answer = 0
    counter = Counter(topping)
    set_dic = set()
    for i in topping:
        counter[i] -= 1
        set_dic.add(i)
        if counter[i] == 0:
            counter.pop(i)
        if len(counter) == len(set_dic):
            answer += 1
    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
# result: 2
topping = [1, 2, 3, 1, 4]
# result: 0

"""
https://school.programmers.co.kr/learn/courses/30/lessons/131704
"""


def solution(order):
    stack = []
    length = len(order)
    idx = 0
    num = 0
    while idx < length:
        if order[idx] > num:
            num += 1
            stack.append(num)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx += 1
        else:
            return idx

    return idx


order = [4, 3, 1, 2, 5]
# result: 2
order = [5, 4, 3, 2, 1]
# result: 5

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12913
"""


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1 :])
    return max(land[-1])


land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
# answer: 16

"""
https://school.programmers.co.kr/learn/courses/30/lessons/154538
"""


def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)
    while dp:
        if y in dp:
            return answer
        else:
            result = set()
            for i in dp:
                if i + n <= y:
                    result.add(i + n)
                if i * 2 <= y:
                    result.add(i * 2)
                if i * 3 <= y:
                    result.add(i * 3)
            dp = result
            answer += 1
    return -1


x = 10
y = 40
n = 5

"""
https://school.programmers.co.kr/learn/courses/30/lessons/12949
"""


def solution(arr1, arr2):
    return [
        [sum(i * j for i, j in zip(col, row)) for col in zip(*arr2)]
        for row in arr1
    ]


arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
# return :	[[15, 15], [15, 15], [15, 15]]
