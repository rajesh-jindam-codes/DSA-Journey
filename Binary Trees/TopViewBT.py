from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

class Solution:
    def topView(self,root):
        if not root:
            return 
        queue=deque()
        ans=[]
        result={}
        queue.append((root,0))
        while queue:
            e,line=queue.popleft()
            if line not in result:
                result[line]=e.val
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1))
        for value in sorted(result.items()):
            ans.append(value[1])
        return ans
obj=Solution()
print(obj.topView(root))