from itertools import permutations

n, m = map(int, input().split())
num = [int(x) for x in input().split()]

arr = []
for i in permutations(num, 3):
    sumNum = sum(i)
    if sumNum > m:
        continue
    arr.append(sumNum)

print(max(arr))