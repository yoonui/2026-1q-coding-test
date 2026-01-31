def check_start_b(arr):
    num = 0
    for i in range(8):
        if i % 2 == 0:
            if arr[i] != 'B':
                num += 1
        else:
            if arr[i] != 'W':
                num += 1
    return num

def check_start_W(arr):
    num = 0
    for i in range(8):
        if i % 2 == 0:
            if arr[i] != 'W':
                num += 1
        else:
            if arr[i] != 'B':
                num += 1
    return num

m, n = map(int, input().split())

arr = []
for i in range(m):
    tmp = input()
    arr.append(tmp)

result = []
for i in range(m - 8 + 1):
    for j in range(n - 8 + 1):
        start_b = 0
        start_w = 0
        for k in range(8):
            if k % 2 == 0:
                start_b += check_start_b(arr[i+k][j:j+8])
                start_w += check_start_W(arr[i+k][j:j+8])
            else:
                start_b += check_start_W(arr[i+k][j:j+8])
                start_w += check_start_b(arr[i+k][j:j+8])
        result.append(start_b)
        result.append(start_w)

print(min(result))