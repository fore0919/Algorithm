# import random

# def lotto_num():
#     lotto = set()
#     while len(lotto) < 6 :
#         lotto.add(random.randint(1,45))
#     lotto = list(lotto) 
#     lotto.sort()

#     return lotto

# print (lotto_num())

# ###### 2차원 리스트 

# lotto_set = []
# def lotto_num(*args):
#     lotto = set()
#     while len(lotto) < 6 :
#         lotto.add(random.randint(1,45))
#     lotto_set.append(sorted(lotto))
#     if len(lotto_set) == 5:
#         return lotto_set
#     else:
#         return lotto_num(lotto_set)

# print (lotto_num())

# ####### 짧은 버전 

# def lotto_num2():
#     for _ in range(5):
#         numbers = sorted(random.sample(range(1,46), 6))
#         print (numbers)
# lotto_num2()


import threading 
x = 0 # A shared value

def foo(): 
    global x 
    for i in range(100000000): 
        x += 1 
def bar(): 
    global x 
    for i in range(100000000): 
        x -= 1 
t1 = threading.Thread(target=foo) 
t2 = threading.Thread(target=bar) 
t1.start() 
t2.start() 
t1.join() 
t2.join() # Wait for completion

print(x)

