num = int(input())
arr = []

for i in range(num):
    str = input()
    arr.append(str)

for i in range(num):
    first = arr.pop(0)
    print(first[0], end="")
    print(first[-1])