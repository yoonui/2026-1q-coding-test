def solution(s):
    answer = 0

    s = list(s)
    first = s[0]
    same, diff = 0, 0

    while s:
        com = s.pop(0)
        if first == com:
            same += 1
        else: diff += 1

        if same == diff:
            answer += 1
            if len(s) > 0: 
                first = s[0]
            same, diff = 0, 0
    
    if same > 0 or diff > 0:
        answer += 1

    return answer

# print(solution("banana"))
print(solution("abracadabra"))
# print(solution("aaabbaccccabba"))