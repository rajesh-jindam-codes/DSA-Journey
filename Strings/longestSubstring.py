def longestSubstring(s):
    hashMap=dict()
    left=0
    right=0
    length=0
    n=len(s)
    while right<n:
        if s[right] in hashMap:
            left=max(hashMap[s[right]]+1,left)
        hashMap[s[right]]=right
        length=max(length,right-left+1)
        right+=1
    return length
print(longestSubstring('ABVUCDSHGADHFC'))