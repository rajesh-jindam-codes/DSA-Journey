m=6
n=5
edges=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]
mydict={}
for i in range(n+1):
    mydict[i]=[]
for u,v in edges:
    mydict[u].append(v)
    mydict[v].append(u)
print(mydict)