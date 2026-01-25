str = input()

answer = 0
a = str.split(" ")
for i in a:
    if i == '':
        continue
    else: answer += 1

print(answer)