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
