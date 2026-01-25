inputStr = input()

for i in range(97, 97+26):
    chrStr = chr(i)
    if chrStr in inputStr:
        print(inputStr.index(chrStr), end=" ")
    else: print("-1", end=" ")