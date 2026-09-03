import heapq
def moveTimes(moveTime):
    rows=len(moveTime)
    cols=len(moveTime[0])
    dist=[[float('inf') for _ in range(cols)]for _ in range(rows)]
    dist[0][0]=0
    queue=[(0,0,0)]
    while queue:
        time,i,j=heapq.heappop(queue)
        if i==rows-1 and j==cols-1:
            return time
        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
            newI,newJ=i+x,j+y
            if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                continue
            newTime=max(time,moveTime[newI][newJ])+1
            if newTime<dist[newI][newJ]:
                dist[newI][newJ]=newTime
                heapq.heappush(queue,(newTime,newI,newJ))
    return -1
print(moveTimes([[0,0,0],[0,0,0]]))
