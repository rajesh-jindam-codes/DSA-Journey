def bellmanFord(V,edges,src):
    inf=10**8
    dist=[inf for _ in range(V)]
    dist[src]=0
    for i in range(V-1):
        for u,v,w in edges:
            if dist[u]!=inf and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
    for u,v,w in edges:
        if dist[u]!=inf and dist[u]+w<dist[v]:
            dist[v]=dist[u]+w
    return dist
V=5
edges=[[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
print(bellmanFord(V,edges,0))