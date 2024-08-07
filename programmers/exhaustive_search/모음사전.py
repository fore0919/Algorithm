"""
https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3#
"""


def solution(word):
    answer = 0
    dic = ["A", "E", "I", "O", "U"]
    temp = [5**i for i in range(len(dic))]
    for i in range(len(word) - 1, -1, -1):
        idx = dic.index(word[i])
        for j in range(5 - i):
            answer += temp[j] * idx
        answer += 1
    return answer


def solution1(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer


from itertools import product


def solution2(word):
    words = []
    for i in range(1, 6):
        for c in product(["A", "E", "I", "O", "U"], repeat=i):
            words.append("".join(list(c)))

    words.sort()
    return words.index(word) + 1


word = "AAAAE"
# result: 6
word1 = "AAAE"
# result: 10
word2 = "I"
# result: 1563
word3 = "EIO"
# result: 1189

print(solution1(word2))
print(solution(word3))
print(solution2(word3))


def solution(word):
    answer = 0
    arr = ["A", "E", "I", "O", "U"]
    num = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += arr.index(word[i]) * num[i] + 1
    return answer


print(solution(word3))
