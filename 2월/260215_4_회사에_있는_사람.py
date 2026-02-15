import sys
input = sys.stdin.readline

n = int(input())
company = set()

for i in range(n):
    s = input().split()
    if s[1] == 'enter':
        company.add(s[0])
    else:
        company.discard(s[0])

for i in sorted(company, reverse=True):
    print(i)