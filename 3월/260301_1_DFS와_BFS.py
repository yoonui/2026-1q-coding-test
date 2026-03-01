from collections import deque

n, m, v = map(int, input().split())

line = dict()
for i in range(m):
    a, b = map(int, input().split())
    
    if a in line:
        line[a].append(b)
        line[a] = sorted(line[a])
    else: line[a] = [b]

    if b in line:
        line[b].append(a)
        line[b] = sorted(line[b])
    else: line[b] = [a]

def dfs(visited, start):
    visited[start] = True
    print(start, end=" ")
    
    if start in line:
        for i in line[start]:
            if visited[i] == False:
                dfs(visited, i)

def bfs():
    queue  = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    print(v, end=" ")

    while queue:
        start = queue.popleft()
        if start in line:
            for i in line[start]:
                if visited[i] == False:
                    print(i, end=" ")
                    visited[i] = True
                    queue.append(i)

dfs([False] * (n+1), v)
print()
bfs()