"""
Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples
Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
"""

import re


def CodelandUsernameValidation(strParam):
    p = re.compile("\w")
    if (
        len(p.findall(strParam)) == len(strParam)
        and strParam[-1] != "_"
        and 4 <= len(strParam) <= 25
        and strParam[0].isalpha()
    ):
        return True
    return False


# keep this function call here
print(CodelandUsernameValidation("aa_"))

"""
Find Intersection
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
the first element will represent a list of comma-separated numbers sorted in ascending order, 
the second element will represent a second list of comma-separated numbers (also sorted). 
Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
If there is no intersection, return the string false.
"""


def FindIntersection(strArr):
    a = strArr[0].split(", ")
    b = strArr[1].split(", ")
    answer = []
    for i in a:
        if i in b:
            answer.append(i)
    if not answer:
        return "false"
    return ",".join(answer)


# keep this function call here
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))

"""
Questions Marks
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, 
and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. 
If so, then your program should return the string true, otherwise it should return the string false. 
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true 
because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
"""


def QuestionsMarks(strParam):
    arr = []
    answer = "true"
    cnt = 0
    for i in range(len(strParam)):
        if strParam[i].isdigit():
            arr.append((i, int(strParam[i])))

    for j in range(1, len(arr)):
        if (arr[j - 1][1] + arr[j][1]) == 10:
            cnt += 1
            if strParam[arr[j - 1][0] : arr[j][0]].count("?") != 3:
                answer = "false"
    if cnt == 0:
        answer = "false"
    return answer


# keep this function call here
print(QuestionsMarks("aa6?9"))
