import sys
input = sys.stdin.readline

n = int(input())
arr1 = {int(x) for x in input().split()}
m = int(input())
arr2 = [int(x) for x in input().split()]

arr2Set = set(x for x in arr2)
ins = arr1 & arr2Set

for i in arr2:
    if i in ins:
        print("1", end=" ")
    else:
        print("0", end=" ")