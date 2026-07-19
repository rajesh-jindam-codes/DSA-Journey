charmap={
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz'
}
result=[]
digits='46'
def solve(index,subset):
    if index==len(digits):
        result.append("".join(subset))
        return
    if digits[index] not in charmap:
        solve(index+1,subset)
        return
    for ch in charmap[digits[index]]:
        subset.append(ch)
        solve(index+1,subset)
        subset.pop()
solve(0,[])
print(result)