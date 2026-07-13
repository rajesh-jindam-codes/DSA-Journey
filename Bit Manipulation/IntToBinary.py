def inttoBinary(num):
    result=""
    while num>0:
        if num%2==1:
            result+='1'
        else:
            result+='0'
        num//=2
    print(result)
inttoBinary(5)