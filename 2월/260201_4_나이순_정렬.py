n = int(input())

members = []
for i in range(n):
    age, name = input().split()
    members.append([i, int(age), name])

members.sort(key=lambda m:(m[1], m[0]))

for i in members:
    print(i[1], i[2])