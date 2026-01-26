num = input()

dialArr = ['', 'ABC','DEF','GHI', 'JKL',' MNO','PQRS','TUV','WXYZ']
answer = 0

for i in num:
    for dir in dialArr:
        if i in dir:
            idx = dialArr.index(dir)
            answer += idx + 2

print(answer)