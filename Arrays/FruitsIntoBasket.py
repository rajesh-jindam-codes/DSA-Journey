def totalFruits(fruits):
    maxLen=0
    n=len(fruits)
    mydict={}
    left=0
    right=0
    while right<n:
        mydict[fruits[right]]=mydict.get(fruits[right],0)+1
        if len(mydict)>2:
            mydict[fruits[left]]-=1
            if mydict[fruits[left]]==0:
                del mydict[fruits[left]]
            left+=1
        if len(mydict)<=2:
            maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
fruits=[3,3,3,1,2,1,1,2,3,4]
print(totalFruits(fruits))