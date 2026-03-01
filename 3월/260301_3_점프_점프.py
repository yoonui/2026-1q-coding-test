from collections import deque

def bfs(s):
    visited = [False] * n
    visited[s] = True
    queue = deque([s])

    while queue:
        start = queue.popleft()
        for i in [-stone[start], stone[start]]:
            node = start+i
            if 0 <= node < n and visited[node] == False:
                visited[node] = True
                queue.append(node)
    print(visited.count(True))

n = int(input())
stone = [int(x) for x in input().split()]
s = int(input())

bfs(s-1)