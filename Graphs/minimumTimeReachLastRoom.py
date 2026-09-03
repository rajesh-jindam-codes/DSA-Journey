import heapq
def moveTime(moveTime):
    rows=len(moveTime)
    cols=len(moveTime[0])
    distance=[[float('inf')]*cols for _ in range(rows)]
    distance[0][0]=0
    heap=[(0,0,0)]
    while heap:
        time,i,j=heapq.heappop(heap)
        if i==rows-1 and j==cols-1:
            return time
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            newI,newJ=i+x,j+y
            if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                continue
            newTime=max(time,moveTime[newI][newJ])+1
            if newTime<distance[newI][newJ]:
                distance[newI][newJ]=newTime
                heapq.heappush(heap,(newTime,newI,newJ))
    return -1
print(moveTime([[0,0,0],[0,0,0]]))