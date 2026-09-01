import heapq
class Solution:
    def minimumEffort(self,heights):
        rows=len(heights)
        cols=len(heights[0])
        effArr=[[float('inf') for _ in range(cols)]for _ in range(rows)]
        effArr[0][0]=0
        queue=[[0,0,0]]
        while len(queue)!=0:
            eff,i,j=heapq.heappop(queue)
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            if i==rows-1 and j==cols-1:
                return eff
            for x,y in directions:
                newI,newJ=i+x,j+y
                if newI<0 or newJ<0 or newI>=rows or newJ>=cols:
                    continue
                newEff=max(eff,abs(heights[i][j]-heights[newI][newJ]))
                if newEff<effArr[newI][newJ]:
                    effArr[newI][newJ]=newEff
                    heapq.heappush(queue,[newEff,newI,newJ])
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(Solution().minimumEffort(heights))
