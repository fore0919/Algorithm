import time

TESTDATA = './etc/버드뷰testdata.txt'

with open (TESTDATA) as f:
    result = f.readlines() # f.readlines(): 개행문자를 기준으로 모든 줄을 읽어서 한 라인씩 리스트로 값을 반환.
    for i in range(10):
        if 'A' in result[i]: # testdata가 문자열 A와 일치하는지 비교
            print('true')
        else:
            print('false')

if __name__ == '__main__':
    data = ['A','B','C','D','E','F','G','H','I','J']
    pass_person = list()

    with open (TESTDATA) as f:
        result = f.readlines()
        for i in range(10): # 열 반복
            time.sleep(0.5) # 0.5초의 간격을 두고 실행 
            for j in data: # 행 반복, 아까 선언한 data리스트와 비교 
                if j in result[i]:
                    print('TRUE, PERSON_INT {}({}), SAME_STR : {}'.format(i, result[i], j))
                else:
                    pass