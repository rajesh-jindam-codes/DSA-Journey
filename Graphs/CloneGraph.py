from collections import deque
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self,node):
        if not node:
            return None
        visited={}
        visited[node]=Node(node.val)
        queue=deque([node])
        while queue:
            curr=queue.popleft()
            for nei in curr.neighbours:
                if nei not in visited:
                    visited[nei]=Node(nei.val)
                    queue.append(nei)
                visited[curr].neighbours.append(visited[nei])
        return visited[node]
adjList = [[2,4],[1,3],[2,4],[1,3]]
obj=Solution()
print(obj.cloneGraph(1))