import sys
input = sys.stdin.readline

n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]

d = dict()
for i in arr1:
    if i in d:
        d[i] += 1
    else: d[i] = 1

for i in arr2:
    if i in d:
        print(d[i], end=" ")
    else: print("0", end=" ")