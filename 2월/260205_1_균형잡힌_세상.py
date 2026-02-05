arr = []
answer = []

while True:
    s = input()
    if s == ".":
        break
    else:
        arr.append(s)

for i in arr:
    if '(' in i or ')' in i or '[' in i or ']' in i:
        stack = []
        no = 0
        for j in i:
            if j == "(" or j == "[":
                stack.append(j)
            elif j == ")":
                if len(stack) > 0:
                    b = stack.pop()
                    if b != "(":
                        no += 1
                        break
                else:
                    no += 1
                    break
            elif j == "]":
                if len(stack) > 0:
                    b = stack.pop()
                    if b != "[":
                        no += 1
                        break
                else:
                    no += 1
                    break
        
        if no > 0 or len(stack) > 0: answer.append("no")
        else: answer.append("yes")
    else: answer.append("yes")

print("\n".join(answer))