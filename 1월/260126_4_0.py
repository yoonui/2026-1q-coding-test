w, h, m = 0, 0, 0
for i in range(9):
    arr = [int(x) for x in input().split()]
    m = max(arr) if max(arr) > m else m
    if m == max(arr):
        w = i+1
        h = arr.index(m)+1

print(m)
print(w, h, end=" ")