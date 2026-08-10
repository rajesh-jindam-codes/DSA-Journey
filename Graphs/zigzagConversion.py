from collections import deque
# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result=[]
        queue=deque([root])
        leftToRight=True
        while queue:
            level=[]
            levelSize=len(queue)
            for i in range(levelSize):
                node=queue.popleft()
                level.append((node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not leftToRight:
                level.reverse()
            result.append(level)
            leftToRight=not leftToRight
        return result

obj=Solution()
# root = [1]
print(obj.zigzagLevelOrder(drinks))