n = input()

result = []
for i in range(len(n)):
    num = int(n[i])
    result.append(num)

result.sort(reverse=True)
for i in result:
    print(i, end="")