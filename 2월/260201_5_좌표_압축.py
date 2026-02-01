n = int(input())

arr = [int(x) for x in input().split()]

unique = sorted(set(arr))
idx = {value:i for i, value in enumerate(unique)}

for i in arr:
    print(idx[i], end=" ")