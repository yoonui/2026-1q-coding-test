dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
m = []
for i in range(n):
    tmp = input()
    m.append(tmp)

visited = [[False] * n for i in range(n)]
answer = []

def dfs(y, x, visited, c):
    visited[y][x] = True
    for i in range(4):
        tmpy = y+dy[i]
        tmpx = x+dx[i]
        if 0 <= tmpy < n and 0 <= tmpx < n and visited[tmpy][tmpx] == False:
            if m[tmpy][tmpx] == "1":
                c = dfs(tmpy, tmpx, visited, c+1)
    return c

for i in range(n):
    for j in range(n):
        if m[i][j] == '0' or visited[i][j] == True:
            continue
        answer.append(dfs(i, j, visited, 1))

answer = sorted(answer)
print(len(answer))
for i in answer:
    print(i)