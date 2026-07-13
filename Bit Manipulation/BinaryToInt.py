def binarytoInteger(x):
    decimalNumber=0
    power=0
    index=len(x)-1
    while index>=0:
        num=int(x[index])*(2**power)
        decimalNumber+=num
        index-=1
        power+=1
    print(decimalNumber)
binarytoInteger('1001')