import sys
input = sys.stdin.readline

n = int(input())

stack = []
out = []
for i in range(n):
    s = input().split()

    if s[0] == "1": stack.append(s[1])
    elif s[0] == "2":
        if len(stack) == 0: out.append("-1")
        else: out.append(stack.pop())
    elif s[0] == "3":
        out.append(str(len(stack)))
    elif s[0] == "4":
        if len(stack) == 0: out.append("1")
        else: out.append("0")
    else:
        if len(stack) == 0: out.append("-1")
        else: out.append(stack[-1])

print("\n".join(out))