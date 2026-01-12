def solution(s, skip, index):
    answer = ''

    for i in s:
        tmp = ord(i)
        for n in range(1, index+1):
            tmp += 1
            if tmp > ord('z'):
                tmp = ord('a')
            while chr(tmp) in skip:
                tmp += 1
                if tmp > ord('z'):
                    tmp = ord('a')
        answer += chr(tmp)

    return answer

# print(solution("aukks", "wbqd", 5))
print(solution("klmnopqrstuvwxyz", "abcdefghij", 20))