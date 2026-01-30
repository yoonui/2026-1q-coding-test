num = int(input())

result = 0
for i in range(num):
    s = i
    strNum = str(i)
    for j in range(len(strNum)):
        s += int(strNum[j])
    if s == num:
        result = i
        break

print(result)