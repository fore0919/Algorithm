"""
https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""


def solution(cacheSize, cities):
    answer = 0
    cached = [None] * cacheSize
    if not cached:
        return len(cities) * 5
    while cities:
        city = cities.pop(0)
        city = city.upper()
        for i in range(len(cached)):
            if city not in cached:
                cached.pop(0)
                cached.append(city)
                answer += 5
                break
            else:
                if cached[i] == city:
                    cached.pop(i)
                    cached.append(city)
                    answer += 1
                    break
    return answer


cacheSize = 3
cities = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
]
# result : 50

"""
https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""
from collections import Counter


def solution(s):
    answer = []
    s = s.replace("{", "").replace("}", "")
    temp = list(map(lambda x: int(x), s.split(",")))
    counter = Counter(temp).most_common()
    for k, v in counter:
        answer.append(k)
    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# result = [2, 1, 3, 4]


"""
https://school.programmers.co.kr/learn/courses/30/lessons/17677
"""


def solution(str1, str2):
    answer = 1

    def change(string):
        array = []
        for s in range(1, len(string)):
            current = string[s - 1].upper() + string[s].upper()
            if current.isalpha():
                array.append(current)
        return array

    str1 = change(str1)
    str2 = change(str2)
    if str1 or str2:
        temp = str1.copy()
        _max = str1.copy()
        _min = []
        for i in str2:
            if i not in temp:
                _max.append(i)
            else:
                temp.remove(i)
        for i in str2:
            if i in str1:
                str1.remove(i)
                _min.append(i)
        answer = len(_min) / len(_max)
    return int(answer * 65536)


str1 = "FRANCE"
str2 = "french"  # Result : 16384

"""
https://school.programmers.co.kr/learn/courses/30/lessons/17687
"""


def solution(n, t, m, p):
    answer = ""
    number = 0

    def func(number, n):
        strings = "0123456789ABCDEF"
        if number < n:
            return strings[number]
        else:
            return func(number // n, n) + strings[number % n]

    while True:
        answer += func(number, n)
        if len(answer) >= t * m:
            answer = answer[: t * m]
            return answer[p - 1 : t * m : m]
        number += 1


n = 2
t = 4
m = 2
p = 1  # result : "0111"

"""
https://school.programmers.co.kr/learn/courses/30/lessons/92335
"""

import math


def solution(n, k):
    answer = 0

    def is_prime(x):
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False
        return True

    def base_number(number, base):
        strings = "0123456789"
        if number < base:
            return strings[number]
        else:
            return base_number(number // base, base) + strings[number % base]

    changed = base_number(n, k)
    temp = changed.split("0")
    for i in temp:
        if not i or i == "1":
            continue
        prime = is_prime(int(i))
        if prime:
            answer += 1
    return answer


n = 437674
k = 3
# result: 3

"""
https://school.programmers.co.kr/learn/courses/30/lessons/17684
"""

from string import ascii_uppercase


def solution(msg):
    answer = []
    strings = [i for i in ascii_uppercase]
    dic = {strings[i]: i + 1 for i in range(len(strings))}
    start, end = 0, 1

    while True:
        if msg[start:end] in dic:
            if end == len(msg):
                answer.append(dic[msg[start:end]])
                break
            end += 1
        else:
            idx = end - 1
            answer.append(dic[msg[start:idx]])
            dic[msg[start:end]] = len(dic) + 1
            start += idx - start
    return answer


msg = "KAKAO"
# answer: [11, 1, 27, 15]
