"""
Example
The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
"""

if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append((name, score))
    arr.sort(key=lambda x: (x[1], x[0]))
    score = list(set(sorted(j for i, j in arr)))[1]
    for i, j in arr:
        if j == score:
            print(i)
