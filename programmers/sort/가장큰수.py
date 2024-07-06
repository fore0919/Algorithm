def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    for n in numbers:
        answer += n
    return str(int(answer))


print(["3", "30", "35"].sort(reverse=True))
numbers = [6, 10, 2]  # result : "6210"
numbers = [3, 30, 34, 5, 9]  # result : "9534330"
print(solution(numbers))
