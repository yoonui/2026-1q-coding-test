import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
answer = []

d = deque([i+1, value] for i, value in enumerate(arr))

while d:
    current = d.popleft()
    i = current[0]
    answer.append(i)

    d.rotate(-current[1]+1 if current[1]>0 else -current[1])

for i in answer:
    print(i, end=" ")