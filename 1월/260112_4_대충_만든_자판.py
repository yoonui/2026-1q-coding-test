def solution(keymap, targets):
    answer = []

    for i in targets:
        sum = 0
        for j in i:
            min = 9999
            for key in keymap:
                if j in key:
                    c = key.index(j)+1
                    if min > c: min = c
            sum += min
            min = 9999
        if sum >= 9999: answer.append(-1)
        else: answer.append(sum)

    return answer

# print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
# print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))