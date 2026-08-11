def customSortCount(order,s):
    count={}
    for ch in s:
        count[ch]=count.get(ch,0)+1
    res=[]
    for ch in order:
        if ch in count:
            res.append(ch*count[ch])
            del count[ch]
    for ch,freq in count.items():
        res.append(ch*freq)
    return "".join(res)
print(customSortCount('cba','abcd'))