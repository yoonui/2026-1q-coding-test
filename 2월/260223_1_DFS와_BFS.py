import sys
from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")

    if start in graph.keys():
        for i in graph[start]:
            if not visited[i]:
                dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=" ")

    while queue:
        v = queue.popleft()

        if start in graph.keys():
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    print(i, end=" ")

input = sys.stdin.readline
n, m, v = map(int, input().split())

g = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a in g:
        g[a].append(b)
    else:
        g[a] = [b]
    g[a] = sorted(g[a])

    if b in g:
        g[b].append(a)
    else:
        g[b] = [a]
    g[b] = sorted(g[b])

visited = [False] * (n+1)
dfs(g, v, visited)

print()

visited = [False] * (n+1)
bfs(g, v, visited)