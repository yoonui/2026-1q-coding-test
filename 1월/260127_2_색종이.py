paper = []
for i in range(100):
    paper.append([0]*100)

num = int(input())

for i in range(num):
    n, m = map(int, input().split())
    for j in range(10):
        for k in range(10):
            paper[m+j][n+k] = 1

sum = 0
for i in range(100):
    for k in range(100):
        if paper[i][k] == 1: sum += 1

print(sum)