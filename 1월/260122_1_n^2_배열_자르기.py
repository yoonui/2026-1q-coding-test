def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        num = max((i//n)+1, (i%n+1))
        answer.append(num)

    return answer

print(solution(3, 2, 5))
# print(solution(4, 7, 14))