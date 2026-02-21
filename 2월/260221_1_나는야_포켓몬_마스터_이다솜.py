import sys
input = sys.stdin.readline

n, m = map(int, input().split())

number = dict()
pokemon = dict()
for i in range(1, n+1):
    s = input().strip()
    number[i] = s
    pokemon[s] = i

for i in range(m):
    s = input().strip()
    if s[0].isalpha():
        print(pokemon[s])
    else:
        print(number[int(s)])