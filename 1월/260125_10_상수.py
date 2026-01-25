left_tmp, right_tmp = input().split()

left = left_tmp[2] + left_tmp[1] + left_tmp[0]
right = right_tmp[2] + right_tmp[1] + right_tmp[0]

if int(left) > int(right):
    print(left)
else: print(right)