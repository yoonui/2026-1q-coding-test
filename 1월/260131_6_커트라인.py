n, k = map(int, input().split())
arr = [int(x) for x in input().split()]

arr.sort(reverse=True)
print(arr[k-1])