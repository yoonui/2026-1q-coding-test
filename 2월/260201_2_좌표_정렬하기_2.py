num = int(input())

arr = []
for i in range(num):
    x,y = map(int, input().split())
    arr.append([x,y])

arr.sort(key=lambda n:(n[1], n[0]))
for i in arr:
    print(i[0], i[1])