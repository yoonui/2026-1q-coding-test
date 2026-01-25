num = int(input())

numArr = []
strArr = []

for i in range(num):
    c, str = input().split()
    numArr.append(int(c))
    strArr.append(str)

for i in range(num):
    numFirst = numArr.pop(0)
    strFirst = strArr.pop(0)
    
    for j in strFirst:
        for k in range(numFirst):
            print(j, end="")
    print()