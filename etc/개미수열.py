import re

# 초기값 = 3, 수열 개수 = 5
# 재귀함수 이용 
def gami(num):
    if num == 1:
        return '3'
    else:
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


def gami2(var): # 다음 수열을 구하는 함수 
    num = var[0] 
    next_num = [] # 다음 수열
    num_cnt = 0 # 이전 숫자의 갯수 

    for i in var: 
        if i is num: # 수열의 현재 항과 num이 같으면 
            num_cnt += 1 # 카운트에 1을 더한다

        else: # 수열의 현재 항과 num이 다르면 
            next_num.append(num) # 다음 수열에 num과 num_cnt를 넣음 
            next_num.append(num_cnt)
            num = i 
            num_cnt = 1

    next_num.append(num)
    next_num.append(num_cnt)

    return next_num

var = [3] # 수열의 초기값 입력

for i in range(0,5): # 수열 개수 입력
    for j in var:
        print(j, end='')
    print() # 반복문 끝나면 출력 
    var = gami2(var) # 다음 수열을 구하는 함수 호출


