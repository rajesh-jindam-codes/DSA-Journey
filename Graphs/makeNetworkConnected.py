class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(0,n+1)]
        self.rank=[0]*(n+1)
    def find(self,x):
        if x==self.parent[x]:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return True
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
        return False
class Solution:
    def makeConnected(self,n,connections):
        ds=DisjointSet(n)
        extraEdges=0
        for u,v in connections:
            if ds.union(u,v):
                extraEdges+=1
        components=0
        for i in range(n):
            if ds.find(i)==i:
                components+=1
        if extraEdges>=components-1:
            return components-1
        return -1
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
obj=Solution()
print(obj.makeConnected(n,connections))