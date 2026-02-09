import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()

for i in range(1, n+1):
    queue.append(i)

answer = []
while queue:
    for i in range(k-1):
        f = queue.popleft()
        queue.append(f)
    answer.append(str(queue.popleft()))

print('<', end="")
print(', '.join(answer), end="")
print('>', end="")