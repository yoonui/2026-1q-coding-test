from collections import deque

n, m, v = map(int, input().split())

line = dict()
for i in range(m):
    a, b = map(int, input().split())
    
    if a in line.keys():
        line[a].append(b)
        line[a] = sorted(line[a])
    else: line[a] = [b]

    if b in line.keys():
        line[b].append(a)
        line[b] = sorted(line[b])
    else: line[b] = [a]


dfsAnswer = []
dfsVisited = [False] * (n+1)

def dfs(start):
    dfsVisited[start] = True
    dfsAnswer.append(start)

    if start in line:
        for i in line[start]:
            if dfsVisited[i] == False:
                dfs(i)

def bfs():
    answer = []
    queue = deque([v])
    visited = [False] * (n+1)
    visited[v] = True

    while queue:
        start = queue.popleft()
        answer.append(start)
        if start in line.keys():
            for i in line[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    for i in answer:
        print(i, end=" ")

dfs(v)
for i in dfsAnswer:
    print(i, end=" ")

print()
bfs()