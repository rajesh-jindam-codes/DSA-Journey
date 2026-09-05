from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def buildTree(self,list):
        if not list:
            return None
        root=TreeNode(list[0])
        queue=deque([root])
        i=1
        while queue and i<len(list):
            curr=queue.popleft()
            if list[i] is not None:
                curr.left=TreeNode(list[i])
                queue.append(curr.left)
            i+=1
            if i<len(list) and list[i] is not None:
                curr.right=TreeNode(list[0])
                queue.append(curr.right)
            i+=1
        return root
list=[1,2,3,4,5,None,7]
root=Solution().buildTree(list)
print(root.val)               # 1
print(root.left.val)          # 2
print(root.right.val)         # 3
print(root.left.left.val)     # 4
