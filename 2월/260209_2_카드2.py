import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()

for i in range(1, n+1):
    d.append(i)

while d:
    if len(d) == 1:
        print(d[0])
        break
    f = d.popleft()
    s = d.popleft()
    d.append(s)