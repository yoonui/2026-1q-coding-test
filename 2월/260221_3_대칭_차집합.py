import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set1 = {int(x) for x in input().split()}
set2 = {int(x) for x in input().split()}

answer = (set1 - set2) | (set2 - set1)
print(len(answer))