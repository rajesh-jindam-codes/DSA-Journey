def palindromeCheck(n):
    def isPalindrome(x):
        return str(x)==str(x)[::-1]
    def isPrime(x):
        if x<2:
            return False
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
            return True
    num=n
    while True:
        if isPalindrome(num) and isPrime(num):
            return num
        num+=1
print(palindromeCheck(6))