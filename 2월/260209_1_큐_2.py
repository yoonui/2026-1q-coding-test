import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
    s = sys.stdin.readline().split()
    s0 = s[0]

    if s0 == 'push':
        queue.append(int(s[1]))
    elif s0 == 'pop':
        if len(queue): print(queue.popleft())
        else: print('-1')
    elif s0 == "size":
        print(len(queue))
    elif s0 == "empty":
        if len(queue): print('0')
        else: print('1')
    elif s0 == "front":
        if len(queue): print(queue[0])
        else: print('-1')
    elif s0 == "back":
        if len(queue): print(queue[-1])
        else: print('-1')
