import sys

n = int(sys.stdin.readline())
queue = [int(x) for x in sys.stdin.readline().split()]

stack = []

tmp = 1
while True:
    if len(stack) == 0 and len(queue) > 0:
        f = queue.pop(0)
        stack.append(f)
    if len(stack) > 0 and len(queue) > 0 and stack[-1] != tmp and queue[0] != tmp:
        f = queue.pop(0)
        stack.append(f)
    if len(stack) > 0 and stack[-1] == tmp:
        stack.pop()
        tmp+=1
    if len(queue) > 0 and queue[0] == tmp:
        queue.pop(0)
        tmp+=1
    
    if len(queue) == 0:
        if len(stack) == 0:
            print("Nice")
            break
        else:
            if stack[-1] != tmp:
                print("Sad")
                break