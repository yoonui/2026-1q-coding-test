def solution(s):
    answer = 0
    sum = 0
    queue = []

    for i in range(len(s)):
        for j in range(i, len(s)+i):
            index = j % len(s)
            now = s[index]

            if now == "(" or now == "[" or now == "{":
                queue.append(now)
            else:
                if len(queue) == 0: continue

                if now == ")" and queue[len(queue)-1] == "(":
                    sum += 1
                    queue.pop()
                if now == "]" and queue[len(queue)-1] == "[":
                    sum += 1
                    queue.pop()
                if now == "}" and queue[len(queue)-1] == "{":
                    sum += 1
                    queue.pop()
        
        if sum > 0 and len(queue) == 0:
            answer += 1
            sum = 0
        queue.clear()
        
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))