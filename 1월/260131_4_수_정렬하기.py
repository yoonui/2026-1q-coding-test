c = int(input())

result = []
for i in range(c):
    num = int(input())
    result.append(num)

result.sort()
for i in result:
    print(i)