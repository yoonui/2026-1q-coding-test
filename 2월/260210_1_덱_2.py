import sys
from collections import deque

d = deque()

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().split()

    if s[0] == '1':
        d.appendleft(s[1])

    elif s[0] == '2':
        d.append(s[1])
    
    elif s[0] == '3':
        if len(d): print(d.popleft())
        else: print("-1")
    
    elif s[0] == '4':
        if len(d): print(d.pop())
        else: print("-1")
    
    elif s[0] == '5':
        print(len(d))
    
    elif s[0] == '6':
        if len(d): print("0")
        else: print("1")
    
    elif s[0] == '7':
        if len(d): print(d[0])
        else: print("-1")
    
    elif s[0] == '8':
        if len(d): print(d[-1])
        else: print("-1")