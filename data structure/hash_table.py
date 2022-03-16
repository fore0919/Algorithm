#### 해시테이블 만들기

hash_table = list([i for i in range(10)])
print (hash_table)

#### 정수만 가져오기 

dataset = [False, 35, 10.5, 2, 56, 'hello']
intdata = [num for num in dataset if type(num) == int]
print (intdata)

#### 간단한 해시 함수 만들기 (division법)

def hash_func(key):
    return key % 5

data1 = 'wecode'
data2 = 'python'
data3 = 'django'
data4 = 'forestella'
data5 = 'miraclass'

print (ord(data1[0]), ord(data2[0]), ord(data3[0]), ord(data4[0]), ord(data5[0])) # ord()아스키코드
print(hash_func(ord(data1[0])), hash_func(ord(data2[0])), hash_func(ord(data3[0])), hash_func(ord(data4[0])), hash_func(ord(data5[0])) )

#### data와 value를 넣으면, 해당 data에 대한 key를 찾아서, 해당 key에 대응하는 해쉬주소에 value를 저장하는 예

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('forest', 'stella')
storage_data('miracle', 'classic')

#### 저장한 데이터 불러오기

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    print (hash_table[hash_address])

get_data('forest')
get_data('miracle')

#### 리스트 변수를 활용해 해시테이블 구현 
#### 해쉬 함수 : key ^% 8 / 해쉬 키 생성 : hash(data)

hash_table1 = list([0 for i in range(8)])
print (hash_table1) # [0, 0, 0, 0, 0, 0, 0, 0] 생성

def get_key1(data1):
    return hash(data1)

def hash_func1(key):
    return key % 8

def save_data(data1, value):
    hash_address1 = hash_func1(get_key1(data1))
    hash_table1[hash_address1] = value

def read_data(data1):
    hash_address1 = hash_func1(get_key1(data1))
    print(hash_address1)  # 1 # 6 
    print(hash_table1[hash_address1]) # 20180314 # 20170926

save_data('forestella95', '20180314')
save_data('miraclass', '20170926')

read_data('forestella95')
read_data('miraclass')

print (hash_table1) # [0, '20180314', 0, 0, 0, 0, '20170926', 0]


#### 충돌 해결 (체이닝 방식)

hash_table1 = list([0 for i in range(8)])
print (hash_table1) # [0, 0, 0, 0, 0, 0, 0, 0] 생성

def get_key1(data1):
    return hash(data1)

def hash_func1(key):
    return key % 8

def save_data(data1, value):
    index_key = get_key1(data1) # indax_key 추가
    hash_address1 = hash_func1(index_key) # 해싱 함수에 대입

    if hash_table1[hash_address1] != 0 : # 해시테이블에 이미 데이터가 들어가 있으면
        for index in range(len(hash_table1[hash_address1])):
            if hash_table1[hash_address1][index][0] == index_key :
                hash_table1[hash_address1][index][1] = value
                return
        hash_table1[hash_address1].append([index_key, value])
    else :
        hash_table1[hash_address1] = [[index_key, value]]

def read_data(data1):
    index_key = get_key1(data1)
    hash_address1 = hash_func1(index_key)

    if hash_table1[hash_address1] != 0 :
        for index in range(len(hash_table1[hash_address1])):
            if hash_table1[hash_address1][index][0] == index_key :
                print (hash_table1[hash_address1][index][1])
        return None
    else :
        return None

save_data('forestella95', '20180314')
save_data('miraclass', '20170926')

read_data('forestella95')
read_data('miraclass')

print (hash_table1) # [0, 0, 0, [[4434678900476293603, '20180314'], [[1422308943645242795], '20170926']], 0, 0, 0, 0]



class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
        
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
    
    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    
    def save(self, key, value):
        hash_address = self.getAddress(key)
        self.hash_table[hash_address] = value
        
    def read(self, key):
        hash_address = self.getAddress(key)
        return self.hash_table[hash_address]
    
    def delete(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
        else:
            return False

h_table = HashTable(8)
h_table.save('a', '1111')
h_table.save('b', '3333')
h_table.save('c', '5555')
h_table.save('d', '8888')
print(h_table.hash_table)
print(h_table.read('d'))

h_table.delete('d')

print(h_table.hash_table)


