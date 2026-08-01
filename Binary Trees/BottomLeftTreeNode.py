from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
drinks=Node('drinks')
hot=Node('hot')
cold=Node('cold')
tea=Node('tea')
coffe=Node('coffe')
cola=Node('cola')
sprite=Node('sprite')
drinks.left=hot
drinks.right=cold
hot.left=tea
hot.right=coffe
cold.left=cola
cold.right=sprite
class Solution:
    def bottomLeft(self,node):
        queue=deque([node])
        ans=node.val
        while queue:
            size=len(queue)
            for i in range(size):
                e=queue.popleft()
                if i==0:
                    ans=e.val
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
        return ans
obj=Solution()
print(obj.bottomLeft(drinks))