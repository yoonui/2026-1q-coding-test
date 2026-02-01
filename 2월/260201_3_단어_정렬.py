num = int(input())

arr = []
for i in range(num):
    s = input()
    if s in arr:
        continue
    arr.append(s)

arr.sort(key=lambda st: (len(st), st))

for i in arr:
    print(i)