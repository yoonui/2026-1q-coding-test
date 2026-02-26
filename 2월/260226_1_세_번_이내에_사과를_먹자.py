from collections import deque

appleMap = []
for i in range(5):
    tmp = [int(x) for x in input().split()]
    appleMap.append(tmp)

r, c = map(int, input().split())
visited = [[False] * 5 for i in range(5)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, move, total):
    visited[r][c] = True
    if appleMap[r][c] == 1:
        total+=1
    if total >= 2: return 1
    if move >= 3:
        visited[r][c] = False
        return 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            if not visited[nr][nc] and appleMap[nr][nc] != -1:
                if dfs(nr, nc, move + 1, total) == 1:
                    return 1
    visited[r][c] = False
    return 0
        

print(dfs(r, c, 0, 0))
