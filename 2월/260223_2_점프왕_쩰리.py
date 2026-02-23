from collections import deque

n = int(input())
gameMap = []
for i in range(n):
    a = [int(x) for x in input().split()]
    gameMap.append(a)

def bfs():
    queue = deque()
    queue.append([0, 0])

    visited = [[False]*n for i in range(n)]

    while queue:
        x, y = queue.popleft()
        if not visited[x][y]:
            if gameMap[x][y] == -1:
                return True
            
            plusX = x + gameMap[x][y]
            plusY = y + gameMap[x][y]

            if plusX < n:
                queue.append([plusX, y])
                visited[x][y] = True
                
            if plusY < n:
                queue.append([x, plusY])
                visited[x][y] = True
    return False

if bfs():
    print("HaruHaru")
else:
    print("Hing")