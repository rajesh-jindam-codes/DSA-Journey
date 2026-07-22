def totalFruits(fruits):
    maxLen=0
    n=len(fruits)
    for i in range(n):
        myset=set()
        for j in range(i,n):
            myset.add(fruits[j])
            if len(myset)>2:
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen

fruits=[3,3,3,1,2,1,1,2,3,4]

print(totalFruits(fruits))    