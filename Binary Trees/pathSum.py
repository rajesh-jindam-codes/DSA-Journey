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
    def hasPathSum(self,root,targetSum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum==root.val
        remaining=targetSum-root.val
        return (
            self.hasPathSum(root.left,remaining) or self.hasPathSum(root.right,remaining)
        )
obj=Solution()
print(obj.hasPathSum(root,10))