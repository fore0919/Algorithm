#### 풀이 1 

def solution(array, commands):
    answer = []
# 2차원 배열 commands가 매개변수로 주어질 때, command(i,j,k)를 뽑음 
    for command in commands:
        i,j,k = command[0],command[1],command[2]
        slice = array[i-1:j] # i번째 수를 인덱싱 하기위해 -1/ slice()함수는 j번째의 직전 인덱스 까지 자르기때문에 -1 하지않음
        slice.sort()
        answer.append(slice[k-1]) # 정렬했던 배열을 인덱싱 
    return answer


#### 풇이 2 

def solution2(array, commands):
    answer = []

    for i in range(len(commands)):
        arr_list = array[commands[i][0]-1:commands[i][1]]
        arr_list.sort()
        answer.append(arr_list[commands[i][2]-1])

    return answer


#### 한줄 풀이 (List Comprehension 이용)

def solution3(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]


#### 한줄 풀이2 (map, lambda 함수 이용)

def solution4(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1 : x[1]])[x[2]-1], commands))

# commands 배열에 map, lambda을 적용해 i, j, k를 뽑음  i= x[0], j = x[1], k = x[2] 
# x[0], x[1]로 slice 후 그 결과를 sorted()를 이용해 정렬.
# x[2]를 이용해 정렬, 결과는 list()로 출력


arr = [1, 5, 2, 6, 3, 7, 4]
comm = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print (solution(arr, comm))
print (solution2(arr, comm))
print (solution3(arr, comm))
print (solution4(arr, comm))
