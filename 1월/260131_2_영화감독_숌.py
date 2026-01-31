def check_six(num):
    lt = str(result)
    if str(result).count('6') >= 3:
        for i in range(len(lt)-2):
            if lt[i] == '6' and lt[i] == lt[i+1] == lt[i+2]:
                return True
    else: return False

num = int(input())

result = 666
idx = 1

while True:
    if idx == num:
        print(result)
        break
    result += 1
    if check_six(result):
        idx+=1