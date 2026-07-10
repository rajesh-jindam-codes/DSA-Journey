n=-123
sign=1
rev=0
if n<0:
    sign=-1
    n=-n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(sign*rev)