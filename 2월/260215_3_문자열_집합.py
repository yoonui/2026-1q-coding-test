import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sSet = set()
num = 0
for i in range(n):
    s = input().strip()
    sSet.add(s)

for i in range(m):
    s = input().strip()
    if s in sSet:
        num += 1

print(num)