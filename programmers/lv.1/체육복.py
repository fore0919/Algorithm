#### 풀이 1
def solution1(n,lost,reserve):
    # 중복값이 없다는 제한 때문에 원소의 값이 unique 하기위해 set사용 # lost = [1,1,2] reserve = [3,3,4] 불가능
    # 여벌이있는(reserve)학생도 도난 당했을 수도 있다는 것은 lost 값에 reserve값이 공통적으로 존재할 수 있다 # lost =[1,2,3],reserve[3,4,5]
    # 3번 학생은 여벌을 빌려줄 수 없음 , 따라서 lost에 reserve와 같은 값이있다면 reserve에서 제외시킴
    set_lost = set(lost) - set(reserve) # 잃어버렸지만 여벌이 있는 학생은 제외
    set_reserve = set(reserve) - set(lost) # 여벌이 있지만 잃어버려서 빌려줄 수 없는 학생은 제외

    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i-1)
        elif i + 1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)

#### 풀이 2 (짧은풀이)
def solution2(n, lost, reserve):
    reserve = set(reserve)

    for size in [0, 1, -2]:
        lost = set(map(lambda x : x+size, lost))
        reserve, lost = reserve - lost, lost - reserve

    return n - len(lost)

#### 풀이 3 (테스트 케이스 4개 실패)
def solution(n,lost,reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for i in set_lost:
        if i + 1 in set_reserve:
            set_reserve.remove(i+1)
        elif i - 1 in set_reserve:
            set_reserve.remove(i-1)
        else:
            n -= 1
    return n

#### 풀이 4 (테스트 케이스 2개 실패)
def solution(n, lost, reserve): 
    _reserve = [r for r in reserve if r not in lost] # 제한사항을 set 자료형으로 안하고 not in 컴프리헨션으로 처리
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)



