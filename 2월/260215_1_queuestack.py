import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arrA = [int(x) for x in input().split()]
arrB = [int(x) for x in input().split()]
m = int(input())
arrC = map(int, input().split())

qs = deque()
for i in range(n):
    if arrA[i] == 0:
        qs.append(arrB[i])

answer = []
for i in arrC:
    qs.appendleft(i)
    answer.append(qs.pop())

print(*answer)