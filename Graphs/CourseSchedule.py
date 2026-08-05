from collections import deque
class Solution:
    def canFinish(self,numCourses,prerequisites):
        adjList=[[] for _ in range(numCourses)]
        indegrees=[0]*numCourses
        for u,v in prerequisites:
            adjList[u].append(v)
        queue=deque()
        result=[]
        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)
        while len(queue)!=0:
            currNode=queue.popleft()
            result.append(currNode)
            for adjNode in adjList[currNode]:
                indegrees[adjNode]-=1
                if indegrees[adjNode]==0:
                    queue.append(adjNode)
        if len(result)==numCourses:
            return True
        return False
obj=Solution()
print(obj.canFinish(2,[[1,0]]))  # Output: True