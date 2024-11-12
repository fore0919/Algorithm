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
