from collections import deque
class Solution:
    def minSteps(self,arr,start,end):
        dist=[float('inf')]*1000
        dist[start]=0
        queue=deque()
        queue.append([0,start])
        while len(queue)!=0:
            step,num=queue.popleft()
            if num==end:
                return step
            for m in arr:
                newNum=(num*m)%1000
                newstep=step+1
                if newstep<dist[newNum]:
                    dist[newNum]=newstep
                    queue.append([newstep,newNum])
        return -1
obj=Solution()
arr=[2,5,7]
start=3
end=30
print(obj.minSteps(arr,start,end))
