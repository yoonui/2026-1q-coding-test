def solution(clothes):
    answer = 1
    dict = {}
    for name, kind in clothes:
        if kind in dict:
            dict[kind] += 1
        else:
            dict[kind] = 1

    for i in dict:
        answer *= dict[i]+1
    
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))