"""
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""


# my answer
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
    return answer


# standard answer
def solution2(phone_book):
    hash_map = {}
    for nums in phone_book:
        hash_map[nums] = 1

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num

            if arr in hash_map and arr != nums:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))  # result: false
