num = int(input())

result = []

for i in range(num//5+1):
    tmp = num
    tmp -= 5*i

    if tmp % 3 == 0:
        result.append(i + tmp // 3)

print(-1 if len(result) == 0 else min(result))