def bellmanFord(V,edges,src):
    INF=10**8
    dist=[INF for _ in range(V)]
    dist[src]=0
    for _ in range(V-1):
        for u,v,w in edges:
            if dist[u]+w <dist[v] and dist[u]!=INF:
                dist[v]=dist[u]+w
    for u,v,w in edges:
        if dist[u]+w<dist[v] and dist[u]!=INF:
            return -1
    return dist
V=5
edges=[[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src=0
print(bellmanFord(V,edges,src))
