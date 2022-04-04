import re

# 초기값 : 3, 수열 개수 : 5 일때
a = '3'
b = ''
for i in range(0, 5):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]: 
            k += 1
        b += str(k-j) + a[j]
        j = k
    print("output:",b)


# 재귀함수 이용 
def gami(num):
        string = gami(num-1)
        result = ''
        start = 0
        while string:
            last = re.search(string[0] + '+', string).end()
            result = result + string[0] + str(last-start)
            string = string[last:]
        return result

for i in range(1,6):
    print (gami(i))