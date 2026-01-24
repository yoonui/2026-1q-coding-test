from itertools import permutations

def check(k, arr):
    for i in arr:
        if k >= i[0]:
            k -= i[1]
        else: return False
    return True

def solution(k, dungeons):
    answer = 0

    for idx in range(1, len(dungeons)+1):
        for i in permutations(dungeons, idx):
            if check(k, i):
                answer = idx

    return answer

# print(solution(80, [[80,20],[50,40],[30,10]]))
print(solution(10, [[9, 2], [10, 3], [7, 3], [5, 4], [1, 1]]))