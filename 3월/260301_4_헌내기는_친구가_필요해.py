from collections import deque

def bfs(x, y, n, m):
    answer = 0
    quene = deque()
    quene.append([x, y])
    visited[y][x] = True

    while quene:
        sx, sy = quene.popleft()
        for i in range(4):
            tmpx = sx + dx[i]
            tmpy = sy + dy[i]
            if 0 <= tmpx < m and 0 <= tmpy < n and visited[tmpy][tmpx] == False:
                if school[tmpy][tmpx] == 'O':
                    visited[tmpy][tmpx] = True
                    quene.append([tmpx, tmpy])
                if school[tmpy][tmpx] == 'P':
                    answer += 1
                    visited[tmpy][tmpx] = True
                    quene.append([tmpx, tmpy])
                if school[tmpy][tmpx] == 'X':
                    visited[tmpy][tmpx] = True

    return answer if answer != 0 else 'TT'



n, m = map(int, input().split())

visited = [[False] * m for i in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

school = []
startX, startY = 0, 0
for i in range(n):
    a = input()

    if 'I' in a:
        startX = a.index('I')
        startY = i

    school.append(a)

print(bfs(startX, startY, n, m))