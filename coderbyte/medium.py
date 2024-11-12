"""
Min Window Substring
Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, 
the first parameter being the string N and the second parameter being a string K of some characters,
and your goal is to determine the smallest substring of N that contains all the characters in K. 
For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string.
So for this example your program should return the string dae.

Examples
Input: ["ahffaksfajeeubsne", "jefaa"]
Output: aksfaje
Input: ["aaffhkksemckelloe", "fhea"]
Output: affhkkse
"""


# hash map 사용
def MinWindowSubstring1(strArr):
    n, k = strArr[0], strArr[1]
    hash_map = {}
    for i in range(len(n)):
        for j in range(i, len(n) + 1):
            cnt = 0
            for x in k:
                if x in n[i:j] and k.count(x) <= n[i:j].count(x):
                    cnt += 1
                    if cnt == len(k):
                        hash_map[len(n[i:j])] = n[i:j]
    return hash_map[min(hash_map.keys())]


# sliding window 사용
def MinWindowSubstring2(strArr):
    n, k = strArr[0], strArr[1]
    answer = n
    window_size = len(k)
    for i in range(len(n) - window_size):
        for idx, val in enumerate(n):
            if any(k.count(x) > n[idx : idx + window_size].count(x) for x in k):
                continue
            answer = min(answer, n[idx : idx + window_size], key=len)
        window_size += 1
    return answer


# keep this function call here
print(MinWindowSubstring1(["ahffaksfajeeubsne", "jefaa"]))
print(MinWindowSubstring2(["aaffhkksemckelloe", "fhea"]))

"""
Tree Constructor
Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: (i1,i2), 
where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1. 
For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:
which you can see forms a proper binary tree. 
Your program should, in this case, return the string true because a valid binary tree can be formed. 
If a proper binary tree cannot be formed with the integer pairs, then return the string false. 
All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.

Examples
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
Output: true
Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
Output: false
"""


def TreeConstructor(strArr):
    a, b = [], []
    for x in strArr:
        i, j = x.replace(")", "").replace("(", "").split(",")
        a.append(i)
        b.append(j)
    for y in range(len(a)):
        if b.count(b[y]) > 2 or len(set(a)) != len(a):
            return "false"
    return "true"


# keep this function call here
print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))

"""
Bracket Matcher
Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for.
Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up.
Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

Examples
Input: "(coder)(byte))"
Output: 0
Input: "(c(oder)) b(yte)"
Output: 1
"""


def BracketMatcher(strParam):
    arr = [i for i in strParam if i in ["(", ")"]]
    q = []
    for i in arr:
        if i == "(":
            q.append(i)
        else:
            if not q:
                return 0
            q.pop(0)
    return 1 if not q else 0


# keep this function call here
print(BracketMatcher("(coder)(byte))"))
