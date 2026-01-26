n, m = map(int, input().split())

left = []
right = []
for i in range(n):
    a = input().split()
    left.append(a)

for i in range(n):
    a = input().split()
    right.append(a)

for i in range(n):
    for j in range(m):
        print(int(left[i][j]) + int(right[i][j]), end=" ")
    print()