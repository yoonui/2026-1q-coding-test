arr = []

for i in range(5):
    str = input()
    arr.append(str)

for i in range(15):
    for j in range(5):
        if i+1 > len(arr[j]): continue
        print(arr[j][i], end="")