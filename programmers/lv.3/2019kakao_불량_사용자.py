
def solution(user_id, banned_id):
    answer = []
    result = [[]]
    for banned in banned_id:
        idx = []
        _list = []
        for i, j in enumerate(banned):
            if j == "*":
                idx.append(i)

        for user in user_id:
            user_name = list(user)
            if len(user) == len(banned):
                for k in idx:
                    user_name[k] = "*"

            user_name = "".join(user_name)
            if user_name == banned:
                for r in result:
                    if user not in r:
                        _list.append(r + [user])
        result = _list

    for name in result:
        if set(name) not in answer:
            answer.append(set(name))

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id2 = ["*rodo", "*rodo", "******"]
user_id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id3 = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))
print(solution(user_id2, banned_id2))
print(solution(user_id3, banned_id3))