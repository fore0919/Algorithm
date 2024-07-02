"""
https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""


def solution(genres, plays):
    answer = []
    hash_map = {}
    hash_map_list = {}
    for i in range(len(genres)):
        hash_map[genres[i]] = hash_map.get(genres[i], 0) + plays[i]
        hash_map_list[genres[i]] = hash_map_list.get(genres[i], []) + [
            (plays[i], i)
        ]
    top_sort = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

    for k, v in top_sort:
        hash_map_list[k] = sorted(hash_map_list[k], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in hash_map_list[k][:2]]

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# result : [4, 1, 3, 0]
