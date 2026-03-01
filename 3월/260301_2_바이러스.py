from collections import deque

computer = int(input())
connect = int(input())

line = dict()
for i in range(connect):
    a, b = map(int, input().split())
    
    if a in line:
        line[a].append(b)
    else: line[a] = [b]

    if b in line:
        line[b].append(a)
    else: line[b] = [a]

visited = [False] * (computer + 1)
def bfs():
    queue = deque([1])
    visited[1] = True

    while queue:
        start = queue.popleft()
        if start in line:
            for i in line[start]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
    print(visited.count(True)-1)

bfs()