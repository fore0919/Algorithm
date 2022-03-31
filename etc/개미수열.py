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



