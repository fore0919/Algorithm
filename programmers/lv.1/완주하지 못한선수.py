#################콜렉션 라이브러리 이용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"] , ["josipa", "filipa", "marina", "nikola"]))

#################해쉬 이용

def solution(participant, completion):
    answer = {}
    for i in participant:
        answer[i] = answer.get(i, 0) +1
    for j in completion:
        answer[j] -= 1
    for k in answer:
        if answer[k] : return k

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"] , ["josipa", "filipa", "marina", "nikola"]))

##################다른사람 풀이 


def solution(participant, completion): 
    hashDict = {} 
    sumHash = 0 
    # 1. Hash : Participant의 dictionary 만들기 
    # # 2. Participant의 sum(hash) 구하기 
    for part in participant: 
        hashDict[hash(part)] = part 
        sumHash += hash(part) 
    # 3. completion의 sum(hash) 빼기 
    for comp in completion: 
        sumHash -= hash(comp) 
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다 
    return hashDict[sumHash]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"] , ["josipa", "filipa", "marina", "nikola"]))

#출처: https://coding-grandpa.tistory.com/85 [개발자로 취직하기]