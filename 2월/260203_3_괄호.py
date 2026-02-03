def check(s):
    stack = []
    all = []

    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack)>0: stack.pop()
            else: return "NO"

    if len(stack) == 0: return "YES"
    else: return "NO"

import sys
input = sys.stdin.readline
n = int(input())

answer = []
for i in range(n):
    s = input()
    answer.append(check(s))

print("\n".join(answer))