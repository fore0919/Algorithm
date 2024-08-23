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

"""
https://school.programmers.co.kr/learn/courses/30/lessons/17686
"""


def solution(files):
    answer = []
    for i in range(len(files)):
        head, number, tail = "", "", ""
        number_check = False
        for j in range(len(files[i])):
            if files[i][j].isdigit():
                number += files[i][j]
                number_check = True
            elif not number_check:
                head += files[i][j]
            else:
                tail += files[i][j:]
                break

        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return ["".join(t) for t in answer]


files = [
    "img12.png",
    "img10.png",
    "img02.png",
    "img1.png",
    "IMG01.GIF",
    "img2.JPG",
]
# answer = ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/42888
"""


def solution(record):
    answer = []
    name = None
    dic = {}
    for r in record:
        array = r.split(" ")
        if array[0] in ["Enter", "Change"]:
            dic[array[1]] = array[2]

    for i in record:
        name = dic[i.split(" ")[1]]
        if i.split(" ")[0] == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        elif i.split(" ")[0] == "Leave":
            answer.append(f"{name}님이 나갔습니다.")
    return answer


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]
# result : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

"""
https://school.programmers.co.kr/learn/courses/30/lessons/118667
"""
from collections import deque


def solution(queue1, queue2):
    answer = 0
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    sum1 = sum(deque1)
    sum2 = sum(deque2)
    limit = len(deque1) * 3

    while sum1 != sum2:
        if answer == limit:
            return -1
        if sum1 > sum2:
            current = deque1.popleft()
            deque2.append(current)
            sum1 -= current
            sum2 += current
        elif sum1 < sum2:
            current = deque2.popleft()
            deque1.append(current)
            sum2 -= current
            sum1 += current
        answer += 1
    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
# result : 2

"""
https://school.programmers.co.kr/learn/courses/30/lessons/92341
"""
import math
from datetime import datetime


def solution(fees, records):

    def parse(time):
        return datetime.strptime(time, "%H:%M")

    answer = []
    parking = {}
    time = {}

    for r in records:
        record = r.split(" ")
        if record[2] == "IN":
            parking[record[1]] = parse(record[0])
        else:
            used_time = (parse(record[0]) - parking[record[1]]).seconds
            time[record[1]] = used_time + time.get(record[1], 0)
            parking.pop(record[1])

    if parking:
        for k, v in parking.items():
            last_time = (parse("23:59") - v).seconds
            time[k] = last_time + time.get(k, 0)

    array = sorted(time.items())
    for k, v in array:
        charge = math.ceil(((v / 60) - fees[0]) / fees[2])
        fee = fees[1] + (max(charge, 0) * fees[3])
        answer.append(fee)
    return answer


"""
https://school.programmers.co.kr/learn/courses/30/lessons/72411
"""
from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        menus = []
        for order in orders:
            menus += combinations(sorted(order), c)
        counter = Counter(menus).most_common()
        for k, v in counter:
            if v > 1 and v == counter[0][1]:
                answer.append("".join(k))
    return sorted(answer)


"""
https://school.programmers.co.kr/learn/courses/30/lessons/17683
"""

from datetime import datetime


def solution(m, musicinfos):

    def parse(x):
        scale = {
            "C#": "1",
            "D#": "2",
            "F#": "3",
            "G#": "4",
            "A#": "5",
            "B#": "6",
        }
        for k, v in scale.items():
            x = x.replace(k, v)
        return x

    answer = []
    m = parse(m)

    for music in musicinfos:
        music = music.split(",")
        time = datetime.strptime(music[1], "%H:%M") - datetime.strptime(
            music[0], "%H:%M"
        )
        length = time.seconds // 60
        music[3] = parse(music[3])
        if length >= len(music[3]):
            x = (
                music[3] * (length // len(music[3]))
                + music[3][: length % len(music[3])]
            )
        else:
            x = music[3][:length]

        if m in x:
            answer.append([music[2], length])

    if not answer:
        return "(None)"
    return sorted(answer, key=lambda x: -x[1])[0][0]


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# answer : "HELLO"

"""
https://school.programmers.co.kr/learn/courses/30/lessons/17679
"""


def solution(m, n, board):
    answer = 0
    _set = set()
    for i in range(m):
        board[i] = list(board[i])

    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                block = board[i][j]
                if not block:
                    continue
                if (
                    board[i][j + 1] == block
                    and board[i + 1][j] == block
                    and board[i + 1][j + 1] == block
                ):
                    _set.add((i, j))
                    _set.add((i, j + 1))
                    _set.add((i + 1, j))
                    _set.add((i + 1, j + 1))
        if _set:
            answer += len(_set)
            for x, y in _set:
                board[x][y] = []
            _set.clear()
        else:
            break

        while True:
            drop = False
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        drop = True
            if not drop:
                break

    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# answer : 14

"""
https://school.programmers.co.kr/learn/courses/30/lessons/60058
"""


def solution(p):
    if not p:
        return ""

    def check(u):
        stack = []
        for i in u:
            if i == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                stack.pop()
        return True

    def divide(arr):
        left, right = 0, 0
        for i in range(len(arr)):
            if arr[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                return arr[: i + 1], arr[i + 1 :]

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        for s in u[1 : len(u) - 1]:
            if s == "(":
                answer += ")"
            else:
                answer += "("
        return answer


p = "(()())()"
# result : "(()())()"


def solution(s):
    answer = []
    if len(s) == 1:
        return len(s)

    for i in range(1, len(s) + 1):
        string = ""
        cnt = 1
        temp = s[:i]
        for j in range(i, len(s) + i, i):
            if temp == s[j : i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    string = string + str(cnt) + temp
                else:
                    string = string + temp
                temp = s[j : j + i]
                cnt = 1

        answer.append(len(string))
    return min(answer)


s = "aabbaccc"
# result: 7

"""
https://school.programmers.co.kr/learn/courses/30/lessons/81302#fnref1
"""


def solution(places):
    answer = []
    for p in range(len(places)):
        temp = []
        for i in range(len(places[p])):
            for j in range(len(places[p][i])):
                if places[p][i][j] == "P":
                    temp.append((i, j))

        check = 1
        while temp:
            r1, c1 = temp.pop(0)
            string = ""
            for r2, c2 in temp:
                if abs(r1 - r2) + abs(c1 - c2) <= 2:
                    if r1 == r2:
                        string += places[p][r2][c2 - 1]
                    elif c1 == c2:
                        string += places[p][r2 - 1][c2]
                    else:
                        string += places[p][r2 + (r1 - r2)][c2]
                        string += places[p][r2][c2 + (c1 - c2)]
            if "O" in string or "P" in string:
                check = 0
                break
        answer.append(check)
    return answer


from itertools import permutations
from re import split

"""
https://school.programmers.co.kr/learn/courses/30/lessons/67257
"""


def solution(expression):
    answer = []
    temp = [i for i in expression if i in ["+", "-", "*"]]
    orders = list(permutations(set(temp), len(set(temp))))
    for order in orders:
        operators = temp.copy()
        numbers = list(map(int, split("[\*\+\-]", expression)))
        for o in order:
            while o in operators:
                i = operators.index(o)
                if o == "*":
                    val = numbers[i] * numbers[i + 1]
                elif o == "+":
                    val = numbers[i] + numbers[i + 1]
                else:
                    val = numbers[i] - numbers[i + 1]
                numbers[i] = val
                numbers.pop(i + 1)
                operators.pop(i)
        answer.append(abs(numbers[0]))
    return max(answer)


"""
https://school.programmers.co.kr/learn/courses/30/lessons/72412
"""

from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    dic = defaultdict(list)

    for infos in info:
        infos = infos.split()
        condition = infos[:-1]
        score = int(infos[-1])

        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                temp = condition.copy()
                for idx in c:
                    temp[idx] = "-"
                k = "".join(temp)
                dic[k].append(score)

    for v in dic.values():
        v.sort()
    for q in query:
        q = q.replace("and", "").split()
        key = "".join(q[:-1])
        value = int(q[-1])
        cnt = 0
        if key in dic:
            arr = dic[key]
            idx = bisect_left(arr, value)
            cnt = len(arr) - idx
        answer.append(cnt)
    return answer
