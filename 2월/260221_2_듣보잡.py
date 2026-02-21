import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = set()
for i in range(n):
    s = input().strip()
    arr1.add(s)

arr2 = set()
for i in range(m):
    s = input().strip()
    arr2.add(s)

answer = arr1 & arr2
print(len(answer))
for i in sorted(answer):
    print(i)