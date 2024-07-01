import math

#### 풀이 1
def solution1(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + days * speeds[0]) >= 100 : # 첫번째 기능이 100이 될때까지 loop  # else: days += 1
            progresses.pop(0) # days가 늘어나다가 100이 되면 요소가 if에 따라 pop 되고 count +=1,  100이 되지않는 요소의 순서가되면 다시 loop하며 +days
            speeds.pop(0)
            count += 1
        else: 
            if count > 0: # 먼저 완성된 기능은 배포 
                answer.append(count) 
                count = 0 # 다시 loop하기 위해 초기화
            days += 1
    answer.append(count) # 마지막 기능 배포
    return answer

#### 풀이 2 
def solution2(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)] # math.ceil(소수점올림)을 활용해서 소요시간 각각 구하고 zip으로 묶어주기.
    answer = []
    front = 0 
    # progresses = [7,3,9]
    for idx in range(len(progresses)): # progresses의 각 소요시간을 확인해서 front 에 가장 오래걸린 소요 시간의 인덱스를 저장하는 반복문. 초기값 0인덱스 
        if progresses[idx] > progresses[front]: # 이전 인덱스 값 보다 다음인덱스 값이 더 커질때까지 
            answer.append(idx - front) # 더 커지면 현재인덱스랑 프론트 인덱스의 차를 구함 
            front = idx # 프론트인덱스를 현재인덱스로 업데이트
            
    answer.append(len(progresses) - front) # 마지막 남은 기능 배포 
    return answer    

#### 풀이 3
def solution3(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


progresses = [93, 30, 55]
speeds = [1, 30, 5] 

print (solution1(progresses, speeds)) 
print (solution2(progresses, speeds))
print (solution3(progresses, speeds))
