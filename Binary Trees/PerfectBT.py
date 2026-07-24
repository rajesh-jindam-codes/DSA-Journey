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
    def isperfect(self,node):
        depth=0
        while node:
            depth+=1
            node=node.left
        return depth
    def findPath(self,root,depth,level=1):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return depth==level
        if root.left is None or root.right is None:
            return False
        return (self.findPath(root.left,depth,level+1) and self.findPath(root.right,depth,level+1))
obj=Solution()
depth=obj.isperfect(root)
print(obj.findPath(root,depth))