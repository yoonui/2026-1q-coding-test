import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())
answer = []

def dfs(y, x):
    field[y][x] = 2
    for i in range(4):
        tmpy = y+dy[i]
        tmpx = x+dx[i]
        if 0 <= tmpy < n and 0 <= tmpx < m and field[tmpy][tmpx] == 1:
            dfs(tmpy, tmpx)

for i in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for i in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    count = 0
    for nn in range(n):
        for mm in range(m):
            if field[nn][mm] == 1:
                dfs(nn, mm)
                count += 1
    print(count)